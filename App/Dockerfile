FROM amazonlinux:latest

MAINTAINER stephenthomas794@gmail.com

RUN yum -y install python3 \
    && pip3 install --upgrade pip

WORKDIR /CordLte

COPY ./flaskr/run.py /flaskr/run.py
COPY . /CordLte

RUN pip3 --no-cache-dir install -r requirements.txt

WORKDIR /CordLte/flaskr
EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["run.py"]
