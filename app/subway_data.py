import json
import logging
import os
from functools import lru_cache

import dotenv
import platformdirs
import protobuf_to_dict
import requests
from google.transit import gtfs_realtime_pb2

_log = logging.getLogger(__name__)

route_to_URL = {
    "1": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
    "2": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
    "3": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
    "4": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
    "5": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
    "6": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
    "7": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs",
    "A": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
    "B": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm",
    "C": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
    "D": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm",
    "E": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace",
    "F": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm",
    "G": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g",
    "J": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz",
    "L": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-l",
    "M": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-bdfm",
    "N": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw",
    "Q": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw",
    "R": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw",
    "W": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw",
    "Z": "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz",
    # 'SIR' : 'https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si',
}
dotenv.load_dotenv(
    dotenv_path=platformdirs.user_config_dir(appname="com.github.ra1993.transitbuddy")
)
mta_subway_key = os.environ.get("MTA_API_KEY", "")

headers = {"x-api-key": mta_subway_key}


@lru_cache
def cached_get(url):
    return requests.get(url, headers=headers)


class SubwayData:
    def __init__(self):
        self.all_train_data = []

    def get_train_data(self):
        for idx, train in enumerate(list(route_to_URL.keys())):
            train_response = cached_get(route_to_URL[train])
            _log.info(f"fetching {route_to_URL[train]=}")

            feed = gtfs_realtime_pb2.FeedMessage()
            feed.ParseFromString(train_response.content)
            self.all_train_data = [
                protobuf_to_dict.protobuf_to_dict(entity) for entity in feed.entity
            ]


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    subway_data_obj = SubwayData()
    subway_data_obj.get_train_data()
    with open("/tmp/wat.json", "w") as outf:
        json.dump(subway_data_obj.all_train_data, outf)
        print(f"Dumped buncha stuff to {outf=}")
