import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os
from time import sleep
from station_data_db.load_station_data_to_db import conn, cur, insert_data

station_data_path = '/home/ra-terminal/datasets/mta_data/stationlocations.csv'
station_data_df = pd.read_csv(station_data_path)

load_dotenv()

class DB_OPS:
    def __init__(self, **kwargs):
        self.conn = conn
        self.cur = cur
        self.sql_st = None
        self.df = None
        pass

    def insert_table_data(self, sql_st, tablename):
        insert_data()

# def create_conn():
#         print('Creating DB connection!')
#         try:
#             conn = psycopg2.connect(
#                 #using docker container i.p to connect locally to it
#                 # host = '192.168.0.2',
#                 host = os.getenv('DB_HOST')
#                 port = os.getenv('DB_PORT', '5432'),
#                 database = os.getenv('DB_NAME'),
#                 user = os.getenv('DB_USER', 'mtapg1'),
#                 password = os.getenv('DB_PASSWORD', '')
#             )
#             print("Connection successful")
#             return conn
#         except psycopg2.OperationalError as e:
#             print("Unable to connect to the database, Retrying")
#             print(e)
#             sleep(5)

# def load_data(conn_obj, cur):
#     print("Fetching data from the database...")
#     query = 'SELECT * FROM subway_station_table;'
#     cur.execute(query)
#     df = pd.DataFrame(cur.fetchall())
#     print("Query executed successfully")

#     return df




if __name__ == '__main__':
    # conn = create_conn()
    # cur = conn.cursor()
    # df = load_data(conn_obj = conn, cur = cur)
    # cur.close()
    # conn.close()
    # print(df.head())
    pass