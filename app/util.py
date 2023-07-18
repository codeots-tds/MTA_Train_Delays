import json
import time
import datetime
import pandas as pd

def save_to_json(entity_data, filename):
    with open(f'/home/ra-terminal/Desktop/portfolio_projects/subway_delays/{filename}.json', 'w') as f_obj:
        json.dump(entity_data, f_obj, indent = 2)

def convert_unix_to_standard_time(unix_time):
    timestamp = datetime.datetime.fromtimestamp(
    int(unix_time)).strftime('%I:%M:%S %p')
    return timestamp

def convert_data_to_df(data_obj):
    df = pd.DataFrame(data_obj)
    return df

if __name__ == "__main__":
    # print(convert_unix_to_standard_time('09:33:58 AM'))
    pass