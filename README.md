# Backfeed Protocol Service Ops

Stuff that has to do with deployment of the REST API

## Install

Clone this repository and cd to the new directory:

    git clone https://github.com/Backfeed/backfeed-restapi-ops.git ops 
    cd ops

If you do not have docker installed, do that first.

### On Linux

    sudo apt-get install docker.io
    sudo service docker start

### On Windows

Install Docker Toolbox from: https://www.docker.com/products/docker-toolbox

## Build

Build the docker image

    docker build -t backfeed-api .

If you get an error like ```dial unix /var/run/docker.sock: connect: permission denied. Are you trying to connect to a TLS-enabled daemon without TLS?```, you may need to add your user to the ```docker``` group:

    usermod -a -G docker {yourusername}

Now you are ready to start the server using the docker image you just created.

You need to tell the docker image (1) which port to listen on and (2) which data directory to use. 

For example, if you want the service to be available on port 8880, and save the data in /home/backfeed/data, you would start the service like tis:

    docker run -it -p 8888:8888 -v /home/backfeed/data:/data backfeed-api

You can now visit your Backfeed REST API at:

    http://0.0.0.0:8888/test/users

If you are satisfied that everything works, you can stop the docker command (with ```ctrl-C``` and then start is in daemon mode:)

    docker run -itd -p 8888:8888 -v /home/backfeed/data:/data backfeed-api


## Deployment in production

If everything is working as it should, 

## Develop

If you want to update your image with the latest versions from master, these work: 

    docker run -it backfeed-api update

You can also login to the docker instance:

    docker run -it backfeed-api /bin/bash 
