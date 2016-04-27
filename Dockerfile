FROM ubuntu:trusty

ENV PYTHONUNBUFFERED 1

RUN apt-get update 
RUN apt-get install -y python python-dev
RUN apt-get install -y curl vim
RUN apt-get install -y python-setuptools
RUN apt-get install -y git
RUN apt-get install -y build-essential python-dev libffi-dev libssl-dev
RUN apt-get install -y runit
RUN apt-get install -y libpq-dev
RUN rm -rf /var/lib/apt/lists/*

# install pip with easy_install, as the trusty repo has a very old version
RUN easy_install -U pip 

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /
RUN pip install -r requirements.txt 

# create the datatabase with database tables# 
VOLUME /data

COPY ./update.sh /bin/update
RUN  chmod a+x /bin/update

COPY ./setup_database.py /bin/setup_database
RUN  chmod u+x /bin/setup_database

COPY ./reload.sh /bin/reload
RUN  chmod u+x /bin/reload

COPY ./development.ini /
COPY ./production.ini /

COPY ./runit.sh /etc/sv/backfeed/run
RUN chmod u+x  /etc/sv/backfeed/run
RUN ln -s /etc/sv/backfeed /etc/service/
# ENTRYPOINT ["runsvdir-start"]
RUN mkdir /var/log/backfeed
RUN touch /var/log/backfeed/debug.log
CMD runsvdir /etc/service && tail -f /var/log/backfeed/debug.log
