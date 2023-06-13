import pandas as pd
import json
import time

from subway_data import subway_data_obj
from google.transit import gtfs_realtime_pb2
from protobuf_to_dict import protobuf_to_dict

from util import save_to_json

class Preprocess_Train_Data:
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
        save_to_json(self.all_subway_data, 'mtatestdata')


    @staticmethod    
    def parse_trip_vehicle_data(subway_data):
        trip_update_list = [] #train trip updates
        vehicle_list  = [] #vehicle info
        train_alerts = [] #train alert messages
        for idx, entity in enumerate(subway_data):
            for key2, item2 in entity.items():
                for idx3, item3 in enumerate(item2):
                    if 'trip_update' in item3.keys():
                        trip_update_list.append(item3)
                    elif 'vehicle' in item3.keys():
                        vehicle_list.append(item3)
                    else:
                        train_alerts.append(item3)

    


        


            


pre_processed_subway_data = Preprocess_Train_Data(all_data = subway_data_obj.all_train_data)
pre_processed_subway_data.parse_feed_data()
pre_processed_subway_data.protobuf_data_to_dict()
fixed_data = pre_processed_subway_data.parse_trip_vehicle_data(pre_processed_subway_data.all_subway_data)
# print(flatted_data)

if __name__ == '__main__':

    print('done')
    pass