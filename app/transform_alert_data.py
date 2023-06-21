import pandas as pd
from preprocess_subway_data import pre_processed_subway_data
import time
import datetime


class Transform_Alert_Data:
    def __init__(self, **kwargs):
        self.alert_data = kwargs.get('data')
        pass

    def flatten_alert_data(self):
        self.alerts = []
        for idx, item in enumerate(self.alert_data):
            alert_text = item['alert']['header_text']['translation'][0]['text']
            alert_row = {'id': item['id'], 'alert_message': alert_text}
            self.alerts.append(alert_row)



if __name__ == '__main__':
    transformed_alert_data = Transform_Alert_Data(data = pre_processed_subway_data.alert_updates)
    transformed_alert_data.flatten_alert_data()
    pass