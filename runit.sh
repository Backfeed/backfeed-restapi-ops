#!/bin/sh

PID=/var/run/gunicorn.pid

if [ -f $PID ]; then rm $PID; fi

cd /
exec gunicorn --pid=$PID --paste  production.ini port=8888 