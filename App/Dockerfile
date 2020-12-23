FROM python:3.9.0

MAINTAINER stephenthomas794@gmail.com

WORKDIR /App

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /App

RUN pip3 install --upgrade pip  

RUN pip3 --no-cache-dir install -r requirements.txt

COPY ./mainApp/run.py /mainApp/run.py
COPY ./mainApp/projects/project1.py /mainApp/projects/project1.py
COPY ./mainApp/static/project1txt /mainApp/static/project1txt

