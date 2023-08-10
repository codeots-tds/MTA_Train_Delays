import pandas as pd
from .preprocess_subway_data import pre_processed_subway_data

from .util import convert_data_to_df
import time
import datetime


class Transform_Alert_Data:
    def __init__(self, **kwargs):
        self.alert_data = kwargs.get('data')
        pass

    def set_id_in_alert_data(self):
        self.alert_updates = []
        for idx, item in enumerate(self.alert_data):
            item['alert']['id'] = item['id']
            del item['id']

    def parse_vehicle_alerts(self):
        trips = []
        for idx, item in enumerate(self.alert_data):
            if 'informed_enetiy' in item['alert']:
                informed_entity = item['alert']['informed_entity']
                for trip in informed_entity:
                    trip['trip']['id'] = item['alert']['id']
                    trip['trip']['alert_description'] = item['alert']['header_text']['translation'][0]['text']
                    trips.append(trip['trip'])
            else:
                print('No Alerts')
        self.alert_data = trips

    def convert_to_df(self):
        self.alert_df = convert_data_to_df(self.alert_data)

transformed_alert_data = Transform_Alert_Data(data = pre_processed_subway_data.alert_updates)
transformed_alert_data.set_id_in_alert_data()
transformed_alert_data.parse_vehicle_alerts()
transformed_alert_data.convert_to_df()
# print(transformed_alert_data.alert_df)

if __name__ == '__main__':
    # transformed_alert_data = Transform_Alert_Data(data = pre_processed_subway_data.alert_updates)
    # transformed_alert_data.flatten_alert_data()
    pass