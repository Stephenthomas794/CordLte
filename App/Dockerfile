FROM python:3.9.0

MAINTAINER stephenthomas794@gmail.com

WORKDIR /App

COPY . /App

RUN pip3 install --upgrade pip  

RUN pip3 --no-cache-dir install -r requirements.txt

COPY ./mainApp/run.py /mainApp/run.py
#COPY ./mainApp/projects /flaskr/projects
COPY ./mainApp/projects/project1.py /mainApp/projects/project1.py

#ONBUILD ADD App/mainApp/projects
#ONBUILD RUN /usr/local/bin/python-build --dir /App/mainApp/projects
#ENV PYTHONPATH /home/ec2-user/CordLte/App/mainApp

CMD ["uwsgi", "app.ini"]
