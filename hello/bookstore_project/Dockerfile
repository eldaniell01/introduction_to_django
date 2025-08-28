# Pull base image
FROM python:3.13

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory
WORKDIR /code

#install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

#copy project
COPY . /code/