import pandas as pd
import datetime
import time
from datetime import datetime as dt

from transform_alert_data import transformed_alert_data
from transform_trip_data import transformed_trip_updates
from transform_vehicle_data import transformed_vehicle_data

"""
Ways to determine if a train is delayed
--looking through the alert data for the train thats late
--looking at the expected arrival time in the trip and compare it with the 
current position of the corresponding train. if timestamp is > than arrival time then late

"""
"""For calculating which trains are delayed"""
class Delayed_Trains:
    def __init__(self, **kwargs):
        self.trip_df = kwargs.get('trip_data')
        self.vehicle_df = kwargs.get('vehicle_data')
        self.alert_df = kwargs.get('alert_data')


    def calculate_train_delays_by_alert(self): #WIP
        list_of_delayed_ids = list(set(self.alert_df['id']))
        delayed_trains_by_alert = self.trip_df[self.trip_df['id'].isin(list_of_delayed_ids)]
        pass

    @staticmethod
    def calc_train_delays(curr_postion_time, expected_arrival_time):
        #current vehicle position time- expected arrival time
        #if current vehicle position is <= then train = early/on time
        #if current vehicle position is >= then train = late
        is_train_delayed = None
        FMT = '%H:%M:%S %p'
        tdelta = dt.strptime(expected_arrival_time, FMT) - dt.strptime(curr_postion_time, FMT)
        if tdelta.total_seconds() >= 0:
            is_train_delayed = False
        else:
            is_train_delayed = True
        return is_train_delayed

    def train_delays_by_vehicle_trip(self):
        train_set_list = set(self.vehicle_df['route_id'])
        self.train_delay_dict = {key: [0] for key in train_set_list}
        trip_id_idx  = {id: idx for idx, id in enumerate(list(self.trip_df['trip_id']))}
        is_train_delayed = None
        for idx, row in self.vehicle_df.iterrows():
            trip_id = row['trip_id']
            curr_pos_time = row['timestamp']
            train = row['route_id']
            date = row['start_date']
            expected_arrival_time = self.trip_df.loc[trip_id_idx[trip_id], 'arrival']
            if trip_id in trip_id_idx.keys():
                is_train_delayed = Delayed_Trains.calc_train_delays(curr_pos_time, expected_arrival_time)
                if is_train_delayed == True:
                    self.train_delay_dict[train][0] += 1
                self.train_delay_dict[train][0] += 0
            if date not in self.train_delay_dict[train]:
                self.train_delay_dict[train].append(date)
            continue
        # print(self.train_delay_dict)

    def build_train_delay_df(self):
        cols = ['train', 'num_of_delays', 'date']
        self.train_delay_df = pd.DataFrame(columns=cols)
        self.train_delay_dict = dict(sorted(self.train_delay_dict.items()))
        self.train_delay_df['train'] = list(self.train_delay_dict.keys())
        for idx, row in self.train_delay_df.iterrows():
            train = row['train']
            if train in list(self.train_delay_dict.keys()):
                self.train_delay_df.iloc[idx, 1:] = self.train_delay_dict[train]
            else:
                continue

if __name__ == '__main__':
    delayed_trains_data = Delayed_Trains(
        trip_data = transformed_trip_updates.trip_df,
        vehicle_data = transformed_vehicle_data.vehicle_df,
        alert_data = transformed_alert_data.alert_df
    )
    delayed_trains_data.train_delays_by_vehicle_trip()
    delayed_trains_data.build_train_delay_df()
    # print(delayed_trains_data.vehicle_df)
    # print(delayed_trains_data.alert_df)
    # print(transformed_vehicle_data.vehicle_df)
    # delayed_trains_data.calculate_train_delays_by_alert()
    pass