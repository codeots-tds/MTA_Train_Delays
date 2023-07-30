import pandas as pd
from create_tables_schemas import *
import psycopg2
import os
import io
from dotenv import load_dotenv
from time import sleep

load_dotenv()

# subway_station_filepath = '/home/ra-terminal/datasets/mta_data/stationlocations.csv'
subway_station_filepath = '/mta_data/stationlocations.csv'
subway_station_df = pd.read_csv(subway_station_filepath)

def create_conn(max_retries = 5):
    retries = 0
    while retries < max_retries:
        try:
            conn = psycopg2.connect(
                host = os.getenv('DB_HOST', 'localhost'),
                port = os.getenv('DB_PORT', '5432'),
                database = os.getenv('DB_NAME'),
                user = os.getenv('DB_USER', 'mtapg1'),
                password = os.getenv('DB_PASSWORD', '')
            )
            print("Connection successful")
            return conn
        except psycopg2.OperationalError as e:
            print("Unable to connect to the database, Retrying")
            print(e)
            sleep(5)
            retries += 1
    return conn

insert_table_query = """COPY {subway_station_table} ({cols}) FROM STDIN WITH (FORMAT CSV, DELIMITER '\t')"""


"""dropping table query"""
drop_data_table = """
DROP TABLE IF EXISTS subway_station_table
"""

def create_table(conn, cur, sql_st):
    try:
        cur.execute(sql_st)
        print(f"""Table {sql_st} was successfully created!""")
        conn.commit()
    except psycopg2.Error as e:
        print("Error: Issue creating table!")
        print(e)

"""insert data function"""
def insert_data(conn, cur, df, sql_st, tablename):
    cols = ','.join(df.columns)
    try:
        buffer = io.StringIO()
        df.to_csv(buffer, index=False, header=False, sep='\t')
        buffer.seek(0)
        cur.copy_from(buffer, f'{tablename}', sep='\t')
        conn.commit()
    except psycopg2.Error as e:
        print("Error: Couldn't load data into postgres")
        print(e)
    else:
        return "Data was loaded!"
    

if __name__ == '__main__':
    conn = create_conn()
    cur = conn.cursor()
    cur.execute(drop_data_table)
    for table_st in create_tables:
         create_table(conn = conn, cur = cur, sql_st = table_st)

    insert_data(conn = conn, cur = cur, df = subway_station_df, sql_st = insert_table_query, tablename='subway_station_table')

    pass