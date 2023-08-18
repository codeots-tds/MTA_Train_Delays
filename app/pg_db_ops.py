import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os
from time import sleep
import station_data_db.load_station_data_to_db as loader

station_data_path = '/home/ra-terminal/datasets/mta_data/stationlocations.csv'
station_data_df = pd.read_csv(station_data_path)

load_dotenv()

class DatabaseOperations:
    def __init__(self, conn = loader.conn, cur = loader.cur, **kwargs):
        self.conn = conn
        self.cur = cur
        self.sql_st = kwargs.get('sql_st')
        self.df = kwargs.get('dataframe')
        self.tablename = kwargs.get('tablename')

    def insert_to_data_table(self):
        loader.insert_data(df = self.df, tablename = self.tablename)

    def update_data_table(self, set_col, set_val, where_col, where_val):
        try:
            update_st = f"UPDATE {self.tablename} SET {set_col} %s WHERE {where_col} = %s;"
            self.cur.execute(update_st, (set_val, where_val))
            self.conn.commit()
        except psycopg2.Error as e:
            print("Error updating row in table:", e)
            
    def check_num_records_in_table(self, tablename):
        query = f"SELECT COUNT(*) FROM  {tablename}"
        count = 0
        try:
            self.cur.execute(query)
            count = self.cur.fetchone([0])
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error fetching number of records from {tablename}:", e)
        return count


    def close_connection(self):
        self.cur.close()
        self.conn.close()

    



if __name__ == '__main__':
    # conn = create_conn()
    # cur = conn.cursor()
    # df = load_data(conn_obj = conn, cur = cur)
    # cur.close()
    # conn.close()
    # print(df.head())
    pass