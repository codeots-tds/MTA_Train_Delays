import json
import time
import datetime
import pandas as pd
from datetime import datetime as dt

def save_to_json(entity_data, filename):
    with open(f'/home/ra-terminal/Desktop/portfolio_projects/subway_delays/{filename}.json', 'w') as f_obj:
        json.dump(entity_data, f_obj, indent = 2)

def convert_unix_to_standard_time(unix_time):
    timestamp = datetime.datetime.fromtimestamp(
    int(unix_time)).strftime('%I:%M:%S %p')
    return timestamp

def convert_data_to_df(data_obj):
    df = pd.DataFrame(data_obj)
    df = df.drop_duplicates()
    return df

def get_time_delta(curr_postime_time, expected_arrival_time):
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(curr_postime_time, FMT) - datetime.strptime(expected_arrival_time, FMT)
    return tdelta

def convert_str_to_date(date_str):
    new_date = dt.strptime(date_str, "%Y%m%d")
    formatted_date = new_date.strftime("%m/%d/%Y")
    return formatted_date

def match_date_to_today():
    pass


if __name__ == "__main__":
    # print(convert_unix_to_standard_time('09:33:58 AM'))
    pass