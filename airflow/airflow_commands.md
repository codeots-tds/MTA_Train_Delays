Configure Airflow's current working directory:
-go into your airflow directory of your current project
-enter: AIRFLOW_HOME=$(pwd)/airflow_home airflow db init

To Start Airflow:
-airflow webserver
-airflow scheduler

-Make sure to configure location of airflow dag folder in airflow.cfg


-initialize your airflow db inside your docker container:
docker exec <your_container_name_or_id> airflow db init

-starting the airflow webserver inside docker:
docker exec <your_container_name_or_id> airflow webserver

-starting airflow scheduler insider docker:
docker exec <your_container_name_or_id> airflow scheduler

OR
-create an entrypoint script that activates airflow webserver/scheduler:




