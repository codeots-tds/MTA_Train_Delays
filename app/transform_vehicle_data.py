import pandas as pd
from preprocess_subway_data import pre_processed_subway_data
from util import convert_data_to_df
import time
import datetime

class Transform_Vehicle_Data:
    def __init__(self, **kwargs):
        self.all_vehicle_updates = kwargs.get('data')

    def flatten_vehicle_data(self):
        vehicle_info = []
        for idx, vehicle_data in enumerate(self.all_vehicle_updates):
            trip_id = vehicle_data['vehicle']['trip']['trip_id']
            start_date = vehicle_data['vehicle']['trip']['start_date']
            route_id = vehicle_data['vehicle']['trip']['route_id']
            curr_stop_seq = vehicle_data['vehicle']['current_stop_sequence']
            current_status = vehicle_data['vehicle']['current_stop_sequence']
            timestamp = vehicle_data['vehicle']['timestamp']
            stop_id = vehicle_data['vehicle']['stop_id']
            vehicle_row_data = {'id': vehicle_data['id'], 
                                'trip_id': trip_id, 
                                'start_date':start_date, 
                                'route_id':route_id,
                                'current_stop_sequence': curr_stop_seq, 
                                'current_status': current_status, 
                                'timestamp': timestamp, 
                                'stop_id' : stop_id}
            vehicle_info.append(vehicle_row_data)    
        self.vehicle_updates = vehicle_info

    def convert_to_df(self):
        self.vehicle_df = convert_data_to_df(self.vehicle_updates)


transformed_vehicle_data = Transform_Vehicle_Data(data = pre_processed_subway_data.vehicle_updates)
transformed_vehicle_data.flatten_vehicle_data()
transformed_vehicle_data.convert_to_df()

if __name__ == '__main__':
    transformed_vehicle_data = Transform_Vehicle_Data(data = pre_processed_subway_data.vehicle_updates)
    transformed_vehicle_data.flatten_vehicle_data()
    transformed_vehicle_data.convert_to_df()
    pass