# Pull base image from python:3
FROM python:3.6

# SET env vars
ENV PYTHONUNBUFFERED 1

# create /code folder
RUN mkdir /code

# copy all source code to /code
ADD Pipfile Pipfile.lock /code/

# install pipenv package manager
RUN python3 -m pip install pipenv

# Change path to app path
WORKDIR /code

# install all dependencies as base path packages
RUN pipenv install --system --dev

# Copy entrypoint
COPY ./docker-entrypoint.sh /docker-entrypoint.sh

# Executable access to entrypoint script
RUN chmod +x /docker-entrypoint.sh