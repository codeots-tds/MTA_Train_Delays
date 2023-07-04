import pandas as pd
import requests as r
import time
from google.transit import gtfs_realtime_pb2
from dotenv import load_dotenv

path_to_env  = '/home/ra-terminal/Desktop/portfolio_projects/subway_delays/.env'
load_dotenv(path_to_env)

train_endpoint_dict = {
    ('A,C,E') : "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
    ('B,D,F,M') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
    ('G') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g',
    ('J','Z') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz',
    ('N','Q','R','W') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
    ('L') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l',
    ('1','2','3','4','5','6','7') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
    # 'SIR' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si',
}

with open('/home/ra-terminal/api_keys/mta_key/mtakey.txt') as f:
    mta_subway_key = f.readlines()[0]

# mta_subway_key = os.environ.get("MTA_API_KEY", "")

class Subway_Data:
    def __init__(self, **kwargs):
        self.all_train_data = []
        pass

    def get_train_data(self):
        headers = {'x-api-key': mta_subway_key}
        feed = gtfs_realtime_pb2.FeedMessage()
        # url_use_dict = Subway_Data.gen_url_dict()

        for idx, train in enumerate(list(train_endpoint_dict.keys())):
            # if url_use_dict[train_endpoint_dict[train]] == 0:
            #     time.sleep(2)
            train_response = r.get(url = train_endpoint_dict[train], headers = headers)
            self.all_train_data.append(train_response.content)
            continue
        # print(self.all_train_data)
            # continue

subway_data_obj = Subway_Data()
subway_data_obj.get_train_data()

if __name__ == "__main__":
    subway_data_obj = Subway_Data()
    subway_data_obj.get_train_data()
    pass