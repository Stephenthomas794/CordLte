FROM python:3.9.0

MAINTAINER stephenthomas794@gmail.com

WORKDIR /App

COPY . /App

RUN pip3 install --upgrade pip  

RUN pip3 --no-cache-dir install -r requirements.txt

COPY ./flaskr/run.py /flaskr/run.py
COPY ./flaskr/projects /flaskr/projects
COPY ./flaskr/projects/project1.py /flaskr/projects/project1.py

ONBUILD ADD App/flaskr/projects
ONBUILD RUN /usr/local/bin/python-build --dir /App/flaskr/projects

ENV PYTHONPATH /home/ec2-user/CordLte/App/flaskr

CMD ["uwsgi", "app.ini"]
