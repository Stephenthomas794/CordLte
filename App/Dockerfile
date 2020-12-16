FROM python:3.9.0

MAINTAINER stephenthomas794@gmail.com

WORKDIR /App

RUN pip3 install --upgrade pip  

COPY ./flaskr/run.py /flaskr/run.py
COPY . /App

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["uwsgi", "app.ini"]
