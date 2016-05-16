# Backfeed Protocol Service Ops

Stuff that has to do with deployment of the REST API

## Install

Clone this repository and cd to the new directory:

    git clone https://github.com/Backfeed/backfeed-restapi-ops.git ops 
    cd ops

If you do not have docker installed, do that first.

### On Debian

You need to install `docker` and `docker-compose`

For Docker, follow the instuctions on https://docs.docker.com/engine/installation/linux/ubuntulinux/
For `docker-compose`, https://github.com/docker/compose/releases

As of writing, this was the quickest way:

    curl -L https://github.com/docker/compose/releases/download/1.7.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

### On Windows

Install Docker Toolbox from: https://www.docker.com/products/docker-toolbox

## Build

The API lives in two docker images - `docker_api` and `docker_postgres`. 

The `.yml` files in the directory where this README file lives are examples of how these docker files can be used. Of particular interest in those files are the `volumes` entries, that define where the data is saved on the host machine. Another entry you might want to look at is the `ports` setting, that maps local ports to ports in the docker files.
 
Building and running the default `docker-compose.yml` file is simply a matter of running:

    docker-compose up

You can now visit your Backfeed REST API at:

    http://0.0.0.0:8888/test/users


## Troubleshooting

If you get an error like ```dial unix /var/run/docker.sock: connect: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS?```, you may need to add your user to the ```docker``` group:

    usermod -a -G docker {yourusername}


## Deployment in production

You probably want to have a cronjob that makes sure the server is started on reboot.

## Develop

If you want to update your image with the latest versions of the `protocol`,  you can use the following commands:

    docker-compose exec backfeed-api update

Restart the protocol service:

    docker-compose exec backfeed-api sv hup backfeed

You can also login to the docker instance:

    docker-compose exec backfeed-api /bin/bash 
