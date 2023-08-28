#!/bin/bash
set -a
#don't have to source the .env file b/c docker-compose.yaml will already be using
#the .env variables
# source ../.env
set +a
# set -e

until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
# exec $cmd
exec "$@"
