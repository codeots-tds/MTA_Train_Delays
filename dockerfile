FROM python:3.9

#working directory in app
WORKDIR /subway_delay_app
#copying all files in app directory
COPY . /app/

#install pipenv, updating bash, postgres
# RUN apt-get update && apt-get -y install python
RUN pip install pipenv
RUN apt-get update && apt-get install -y postgresql-client

# Copy files over
COPY Pipfile Pipfile.lock ./
COPY ./bin/wait_for_pg_db.sh ./bin/wait_for_pg_db.sh
COPY ./.env ./app/.env

# Run/Install dependencies
RUN pipenv install --verbose
RUN chmod +x ./bin/wait_for_pg_db.sh

EXPOSE 80

# Define the command to run your app using CMD which defines your runtime
# Replace 'your-command-here' with your own command
# CMD ["./bin/wait_for_pg_db.sh"]
CMD ["sleep", "800"]