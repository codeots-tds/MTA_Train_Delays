FROM python:3.9
#This is the dockerfile for the app service. The reason why docker build is throwing an error
#is b/c docker build can't access parent directories for security reasons so thats why it can't access 
# bin/wait_for_pg_db.sh script which is in the root directory. Now I have to move this dockerfile to the root directory.
#another way to mitigate this is to run the docker build command at root directory.

# Set the working directory in the container to /app
WORKDIR /app

# Copy the contents of the app directory into the container's /app directory
COPY ./app ./app

# Copy the wait_for_pg_db.sh script from the bin directory on the host into the /app/bin directory in the container
COPY ./bin/wait_for_pg_db.sh ../bin/

# Update and install necessary packages
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/* 

# Install pipenv
RUN pip install pipenv

# Install dependencies from Pipfile
RUN pipenv install

# Make the wait_for_pg_db.sh script executable
RUN chmod +x ../bin/wait_for_pg_db.sh

# Expose port 80
EXPOSE 80

# Set the CMD to run the script when the container starts
CMD ["sh", "../bin/wait_for_pg_db.sh"]