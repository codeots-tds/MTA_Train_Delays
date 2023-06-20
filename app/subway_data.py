import pandas as pd
import requests as r
import time
from google.transit import gtfs_realtime_pb2
import dotenv

# dotenv.load_dotenv(dotenv_path=platformdirs.user_config_dir(appname="Subway_Delay"))
train_endpoint_dict = {
    ('A,C,E') : "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
    ('B,D,F,M') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
    ('G') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g',
    ('J','Z') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz',
    ('N','Q','R','W') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
    ('L') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l',
    ('1','2','3','4','5','6','7') : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs'
}


# train_endpoint_dict = {
#         'A' : "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
#         'C' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace',
#         'E' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace',
#         'B' :'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
#         'D' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
#         'F' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
#         'M' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm',
#         'G' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g',
#         'J' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz',
#         'Z' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz',
#         'N' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
#         'Q' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
#         'R' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
#         'W' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw',
#         'L' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l',
#         '1' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
#         '2' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
#         '3' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
#         '4' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
#         '5' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
#         '6' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
#         '7' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs',
#         # 'SIR' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si',
#     }
with open('/home/ra-terminal/api_keys/mta_key/mtakey.txt') as f:
    mta_subway_key = f.readlines()[0]

# mta_subway_key = os.environ.get("MTA_API_KEY", "")

class Subway_Data:
    def __init__(self, **kwargs):
        self.all_train_data = []
        pass
    
    # @staticmethod
    # def gen_url_dict():
    #     url_use_dict = {}
    #     for k, v in train_endpoint_dict.items():
    #         if v not in url_use_dict.keys():
    #             url_use_dict[v] = 0
    #     return url_use_dict


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