#!/bin/bash
set -e

# Initialize the database
airflow db init

# Create airflow user if not exists
airflow users create \
    --username $AIRFLOW_USERNAME \
    --firstname $AIRFLOW_FIRST_NAME \
    --lastname $AIRFLOW_LAST_NAME \
    --role $ROLE \
    --email $EMAIL \
    --password $AIRFLOW_PASS

# Start the web server, with N worker processes and -D argument to run it as a daemon
airflow webserver -D

# Start the scheduler, also with the -D argument
airflow scheduler -D

# The container will execute the following command if the user specifies arguments to docker run
exec "$@"
