import pandas as pd
import json
import time

from subway_data import subway_data_obj
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict

from util import save_to_json
import time

class General_Preprocessing:
    def __init__(self, **kwargs):
        self.data = kwargs.get('all_data')

    def convert_time(self):
        pass

    def convert_date(self):
        pass



class Preprocess_MTA_Data:
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
#--------

#general trip preprocessing
# general_preprocessed = General_Preprocessing(all_data = pre_processed_subway_data.trip_updates)
# general_preprocessed.remove_time_dict(key1 = 'trip_update', key2 = 'stop_time_update')



if __name__ == '__main__':

    print('done')
    pass