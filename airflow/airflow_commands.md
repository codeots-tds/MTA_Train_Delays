1. Configure Airflow's current working directory:
--go into your airflow directory of your current project
--enter: AIRFLOW_HOME=$(pwd)/airflow_home airflow db init

-To Start Airflow:
--airflow webserver
--airflow scheduler

2. Make sure to configure location of airflow dag folder in airflow.cfg


3. initialize your airflow db inside your docker container:
--docker exec <your_container_name_or_id> airflow db init

4. starting the airflow webserver inside docker:
--docker exec <your_container_name_or_id> airflow webserver

5. starting airflow scheduler insider docker:
--docker exec <your_container_name_or_id> airflow scheduler

OR

6. create an entrypoint script that activates airflow webserver/scheduler:

7. to create airflow user and password, put in terminal:
docker exec -it <container_name_or_id> airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@example.com

or you can enter/create credentials in the airflow dockerfile, and put credential inputs in your .env file.

8. docker compose commands:
- docker-compose --build (rebuilds containers with cache)
- docker-compose build --no-cache (docker usually caches to build containers more quickly, so this rebuilds your container without caching)
- docker-compose up --build (builds/rebuilds containers and starts them)
- docker-compose up (starts all containers)



