FROM python:3.8

#working directory in app
WORKDIR /app
#copying all files in app directory
COPY . /app/

#install pipenv
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock file
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --verbose

# Define the command to run your app using CMD which defines your runtime
# Replace 'your-command-here' with your own command
CMD ["python"]

