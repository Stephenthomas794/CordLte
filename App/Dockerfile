FROM python:3.9.0

MAINTAINER stephenthomas794@gmail.com

WORKDIR /App

RUN pip3 install --upgrade pip  

COPY ./flaskr/run.py /flaskr/run.py
COPY ./flaskr/projects/project1.py /flaskr/projects/project1.py
COPY . /App

RUN pip3 --no-cache-dir install -r requirements.txt

ENV PYTHONPATH "/home/ec2-user/CordLte/App/flaskr:/home/ec2-user/CordLte/App/flaskr/projects"

CMD ["uwsgi", "app.ini"]
