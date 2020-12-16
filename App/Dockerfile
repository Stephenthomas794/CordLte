FROM python:latest

MAINTAINER stephenthomas794@gmail.com

RUN yum -y install python3 \
    && pip3 install --upgrade pip

WORKDIR /App

COPY ./flaskr/run.py /flaskr/run.py
COPY . /App

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["uwsgi", "run.py"]
