import pandas as pd
import json


from .subway_data import subway_data_obj
from .pg_db_ops import station_data_df
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict
from .util import *

import datetime


class General_Preprocessing:
    def __init__(self, **kwargs):
        self.data = kwargs.get('all_data')

    def convert_time_data(self):
        for trip in self.trip_updates:
            stop_time_update_list = trip['trip_update']['stop_time_update']
            for time_data in stop_time_update_list:
                if 'arrival' in time_data.keys():
                    arrival_time = time_data['arrival']['time']
                    # arrival_time = datetime.datetime.fromtimestamp(
                    # int(arrival_time)).strftime('%I:%M:%S %p')
                    arrival_time = convert_unix_to_standard_time(arrival_time)
                    time_data['arrival'] = arrival_time
                if 'departure' in time_data.keys():
                    departure_time = time_data['departure']['time']
                    # departure_time = datetime.datetime.fromtimestamp(
                    # int(departure_time)).strftime('%I:%M:%S %p')
                    departure_time = convert_unix_to_standard_time(departure_time)
                    time_data['departure'] = departure_time

        for vehicle_data in self.vehicle_updates:
            timestamp = vehicle_data['vehicle']['timestamp']
            timestamp = datetime.datetime.fromtimestamp(
                    int(timestamp)).strftime('%I:%M:%S %p')
            vehicle_data['vehicle']['timestamp'] = timestamp

    def replace_stop_ids_with_station_names(self):
        stop_id_station_dict = station_data_df.set_index('GTFS Stop ID')['Stop Name'].to_dict()
        for trip in self.trip_updates:
            stop_time_update_list = trip['trip_update']['stop_time_update']
            for idx, stop_data in enumerate(stop_time_update_list):
                bound = None
                stop = None
                stop_id = stop_data['stop_id']
                stop = stop_id[:-1]
                bound = stop_id[-1]
                if stop in stop_id_station_dict.keys():
                    stop_data['stop_id'] = f'''{stop_id_station_dict[stop] + '--' + bound}'''

        for vehicle_data in self.vehicle_updates:
            bound2 = None
            stop2 = None
            stop_id_v = vehicle_data['vehicle']['stop_id']
            stop2 = stop_id_v[:-1]
            bound2 = stop_id_v[-1]
            if stop2 in stop_id_station_dict.keys():
                vehicle_data['vehicle']['stop_id'] = f'''{stop_id_station_dict[stop2] + '--' + bound2}'''



class Preprocess_MTA_Data(General_Preprocessing):
    def __init__(self, **kwargs):
        self.all_subway_data = kwargs.get('all_data')
        self.subway_data = []
        pass

    def parse_feed_data(self):
        feed = gtfs_realtime_pb2.FeedMessage()
        for idx, data in enumerate(self.all_subway_data):
            feed.ParseFromString(data)
            # print(feed)
            self.all_subway_data[idx] = feed
        # print(self.all_subway_data)
        # print(len(self.all_subway_data) ,len(self.all_subway_data))

    def protobuf_data_to_dict(self):
        protobuffed_data = []
        for idx, data in enumerate(self.all_subway_data):
            protobuf_data = protobuf_to_dict(data)
            if 'header' in protobuf_data.keys():
                del protobuf_data['header']
            # if 'entity' in protobuf_data.keys()
            protobuffed_data.append(protobuf_data)
        self.all_subway_data = protobuffed_data
        #for testing
        # save_to_json(self.all_subway_data, 'mtatestdata')

 
    def parse_trip_vehicle_data(self): #needs to be refactored
        self.trip_updates = [] #trips
        self.vehicle_updates = [] #vehicles
        self.alert_updates = [] #alert
        for idx, entity in enumerate(self.all_subway_data):
            for key2, item2 in entity.items():
                # print(item2)
                for idx3, item3 in enumerate(item2):
                    if 'trip_update' in item3.keys():
                        self.trip_updates.append(item3)
                    elif 'vehicle' in item3.keys():
                        self.vehicle_updates.append(item3)
                    else:
                        self.alert_updates.append(item3)

# Subway preprocessing
pre_processed_subway_data = Preprocess_MTA_Data(all_data = subway_data_obj.all_train_data)
pre_processed_subway_data.parse_feed_data()
pre_processed_subway_data.protobuf_data_to_dict()
pre_processed_subway_data.parse_trip_vehicle_data()
pre_processed_subway_data.replace_stop_ids_with_station_names()
pre_processed_subway_data.convert_time_data()
#--------



if __name__ == '__main__':
    print(pre_processed_subway_data.all_subway_data)
    print('done')
    pass