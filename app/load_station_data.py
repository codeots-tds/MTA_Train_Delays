import psycopg2
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

def create_conn():
    conn = psycopg2.connect(
        # host = 'DB_HOST',
        database = os.getenv('DB_NAME'),
        user = os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        port = '5432',
    )
    return conn

def load_stop_id_and_station_name(conn_obj, col_names):
    cur = conn_obj.cursor()
    query = f'''SELECT stop_id, station_name FROM subway_station_table;'''
    cur.execute(query)
    data = cur.fetchall()
    # df = pd.read_sql(f'SELECT {col_names} FROM subway_station_table', con = conn_obj)
    cur.close()
    conn.close()
    print(data)



if __name__ == '__main__':
    conn = create_conn()
    df = load_stop_id_and_station_name(conn_obj = conn, col_names= ['stop_id', 'station_name'])

    pass