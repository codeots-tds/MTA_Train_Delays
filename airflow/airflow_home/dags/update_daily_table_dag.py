import sys
sys.path.append("/home/ra-terminal/Desktop/portfolio_projects/subway_delays")

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from datetime import datetime
from app.pg_db_ops import DatabaseOperations
from calculate_delayed_trains_dag import generate_delayed_trains_report
from app.util import *
import psycopg2
import logging


def get_report_date(df):
    current_date = df['date'][0]
    return current_date


def load_data_daily_delay_table():
    daily_report_df = generate_delayed_trains_report()
    tablename = 'daily_delays_table'
    logging.info("Starting to load daily delay data.")
    try:
        if DatabaseOperations.check_num_records_in_table(tablename = 'daily_delays_table') == 0:
            DatabaseOperations.insert_to_data_table(df = daily_report_df, tablename = tablename)
        else:
            query = """
            INSERT INTO daily_delays_table (train, date, num_of_delays)
            VALUES (%s, %s, %s)
            ON CONFLICT (train, date) DO UPDATE 
            SET num_of_delays = EXCLUDED.num_of_delays
        """
            rows_to_insert = list(daily_report_df.itertuples(index=False))
            with DatabaseOperations.get_connection() as conn:
                with conn.cursor() as cursor:
                    cursor.executemany(query, rows_to_insert)
                    conn.commit()
        logging.info("Data loaded successfully.")
    except Exception as e:
        logging.error(f"Error occurred while loading data: {e}")
    return "Data loaded successfully"

default_args = {
    'owner' : 'me',
    'start_date' : datetime(2023, 1, 23),
    'retries' : '3'
}

dag = DAG(
    'update_daily_delay_table',
    default_args = default_args,
    description = 'DAG to update subway delay report',
    schedule_interval = '@hourly',
    catchup = False
)

generate_delay_report_task = PythonOperator(
    task_id = 'update_daily_table_task',
    python_callable = load_data_daily_delay_table,
    dag = dag,
    )

wait_for_calculate_delayed_trains_dag = ExternalTaskSensor(
    task_id="wait_for_calculate_delayed_trains_dag_task",
    external_dag_id="calculate_delayed_trains_dag",
    external_task_id="generate_delayed_trains_task",
    mode="poke",
    poke_interval=60,  # check every 60 seconds
    timeout=3600,  # timeout after an hour
    dag=dag
)

wait_for_calculate_delayed_trains_dag >> generate_delay_report_task
