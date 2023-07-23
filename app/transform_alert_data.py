import pandas as pd
from preprocess_subway_data import pre_processed_subway_data

from util import convert_data_to_df
import time
import datetime


class Transform_Alert_Data:
    def __init__(self, **kwargs):
        self.alert_data = kwargs.get('data')
        pass

    def flatten_alert_data(self):
        self.alert_updates = []
        for idx, item in enumerate(self.alert_data):
            alert_text = item['alert']['header_text']['translation'][0]['text']
            alert_row = {'id': item['id'], 'alert_message': alert_text}
            self.alert_updates.append(alert_row)

    def convert_to_df(self):
        self.alert_df = convert_data_to_df(self.alert_updates)

transformed_alert_data = Transform_Alert_Data(data = pre_processed_subway_data.alert_updates)
transformed_alert_data.flatten_alert_data()
transformed_alert_data.convert_to_df()


if __name__ == '__main__':
    # transformed_alert_data = Transform_Alert_Data(data = pre_processed_subway_data.alert_updates)
    # transformed_alert_data.flatten_alert_data()
    pass