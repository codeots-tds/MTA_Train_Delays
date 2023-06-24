import pandas as pd

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
        self.delay_dict = {}
        self.delay_df = pd.DataFrame()

    def calculate_train_delays_by_alert(self):
        list_of_delayed_ids = list(set(self.alert_df['id']))
        delayed_trains_by_alert = self.trip_df[self.trip_df['id'].isin(list_of_delayed_ids)]
        pass

    def calculate_train_delays_by_vehicle_time(self):
        
        pass



if __name__ == '__main__':
    delayed_trains_data = Delayed_Trains(
        trip_data = transformed_trip_updates.trip_df,
        vehicle_data = transformed_vehicle_data.vehicle_df,
        alert_data = transformed_alert_data.alert_df
    )
    # print(delayed_trains_data.vehicle_df)
    # print(delayed_trains_data.alert_df)
    # print(transformed_vehicle_data.vehicle_df)
    delayed_trains_data.calculate_train_delays_by_alert()
    pass