# syntax=docker/dockerfile:1
FROM python:3
#python-dotenv

RUN mkdir /app
WORKDIR /app

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install python-dotenv
RUN pip3 install flask

EXPOSE 5000

RUN flask run --host=0.0.0.0
