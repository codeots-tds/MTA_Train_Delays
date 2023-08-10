Configure Airflow's current working directory:
-go into your airflow directory of your current project
-enter: AIRFLOW_HOME=$(pwd)/airflow_home airflow db init

To Start Airflow:
-airflow webserver
-airflow scheduler

-Make sure to configure location of airflow dag folder in airflow.cfg


