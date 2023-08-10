import sys
sys.path.append("/home/ra-terminal/Desktop/portfolio_projects/subway_delays")

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from app.calculate_delayed_trains import Delayed_Trains
from app.transform_alert_data import transformed_alert_data
from app.transform_trip_data import transformed_trip_updates
from app.transform_vehicle_data import transformed_vehicle_data

def generate_delayed_trains_report():
    delayed_trains_report = Delayed_Trains(
        trip_data = transformed_trip_updates.trip_df,
        vehicle_data = transformed_vehicle_data.vehicle_df,
        alert_data = transformed_alert_data.alert_df
    )
    delayed_trains_report.train_delays_by_vehicle_trip()
    delayed_trains_report.calculate_train_delays_by_alert()
    delayed_trains_report.build_train_delay_df()
    return delayed_trains_report.train_delay_df


default_args = {
    'owner' : 'me',
    'start_date' : datetime(2023, 1-1-23),
    'retries' : '3'
}

dag = DAG(
    'calculate_delayed_trains_dag',
    default_args = default_args,
    description = 'DAG to generate subway delay report',
    schedule_interval = '@hourly',
    catchup = False
)

generate_delay_report_task = PythonOperator(
    task_id = 'generate_delayed_trains_task',
    python_callable = generate_delayed_trains_report,
    dag = dag,
    )

if __name__ == '__main__':
    # print(generate_delayed_trains_report().trip_df)
    pass