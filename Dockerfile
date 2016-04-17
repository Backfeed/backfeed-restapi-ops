FROM ubuntu:trusty

ENV PYTHONUNBUFFERED 1

RUN apt-get update 
RUN apt-get install -y python python-dev
RUN apt-get install -y curl vim
RUN apt-get install -y python-setuptools
RUN apt-get install -y git
RUN apt-get install -y build-essential python-dev libffi-dev libssl-dev
# RUN  rm -rf /var/lib/apt/lists/*

# install pip with easy_install, as the trusty repo has a very old version
RUN easy_install -U pip 

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /
RUN pip install -r requirements.txt 


# create the datatabase with database tables# 
VOLUME /data
# COPY ./setup_database.py /
# RUN python setup_database.py "/data/backfeed.db"

#
# remove this when done debugging
#

# COPY ./src /src
# RUN pip install -e /src/backfeed_protocol/
# RUN pip install -e /src/restapi

COPY ./development.ini /
COPY ./production.ini /
CMD gunicorn --paste development.ini port=8888