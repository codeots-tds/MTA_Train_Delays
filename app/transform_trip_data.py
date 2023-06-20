import pandas as pd
from preprocess_subway_data import pre_processed_subway_data


class Transform_Trip_Data:
    def __init__(self, **kwargs):
        self.trip_updates = kwargs.get('trip_list')

    def add_id_to_trip(self):
        for idx, trip in enumerate(self.trip_updates):
            trip['trip_update']['trip']['id'] = trip['id']
            del trip['id']

    # def create_trip_id_dict(self):    
    #     self.trip_id_dict = {}
    #     for idx, trip in enumerate(self.trip_updates):
    #         trip_id = trip['trip_update']['trip']['trip_id']
    #         self.trip_id_dict[trip_id] = trip
    #         del trip['trip_update']['trip']['trip_id']

    def parse_arrival_and_departure(self):
        #may need to remove stop_id_arrival for ones that show both arrival and departure
        for idx, trip_update in enumerate(self.trip_updates):
            for key, trip in trip_update.items():
                times_list = trip['stop_time_update']
                for times_dict in times_list:
                    if ['arrival', 'departure', 'stop_id'] in list(times_dict.keys()):
                        trip_update[key]['trip']['arrival'] = times_dict['arrival']
                        trip_update[key]['trip']['departure'] = times_dict['departure']
                        trip_update[key]['trip']['stop_id_both'] = times_dict['stop_id']
                    elif 'arrival' in times_dict.keys() and 'departure' not in times_dict.keys():
                        trip_update[key]['trip']['arrival'] = times_dict['arrival']
                        trip_update[key]['trip']['stop_id_arrival'] = times_dict['stop_id']
                    elif 'departure' in times_dict.keys() and 'arrival' not in times_dict.keys():
                        trip_update[key]['trip']['departure'] = times_dict['departure']
                        trip_update[key]['trip']['stop_id_departure'] = times_dict['stop_id']
                del trip['stop_time_update']           

    def remove_extra_keys(self):
        final_trip_list = []
        for idx, trip_update in enumerate(self.trip_updates):
            flat_data = trip_update['trip_update']['trip']
            final_trip_list.append(flat_data)
        self.trip_updates = final_trip_list

    def convert_to_df(self):
        # print(self.trip_updates)
        # print('-------')
        # print(self.trip_updates[50])
        df = pd.DataFrame(self.trip_updates)
        print(df.head(5))


    def trip_dict_to_df(self):
        pass

transformed_trip_updates = Transform_Trip_Data(trip_list = pre_processed_subway_data.trip_updates)
transformed_trip_updates.add_id_to_trip()
# transformed_trip_updates.create_trip_id_dict()
transformed_trip_updates.parse_arrival_and_departure()
transformed_trip_updates.remove_extra_keys()
transformed_trip_updates.convert_to_df()