# Backfeed Protocol Service Ops

Stuff that has to do with deployment of the REST API

## Installation

Clone this repository and cd to the new directory:

    git clone https://github.com/Backfeed/backfeed-restapi-ops.git ops 
    cd ops

If you do not have docker installed, do that first:

    sudo apt-get install docker.io
    sudo service docker start

Build the docker image

    docker build -t backfeed-restapi-service .

Now start the docker image.

You need to tall the docker image (1) which port to listen on and (2) which data directory to use.

    docker run -itd -p 8888:8888 backfeed-restapi-service 

You can then visit your Backfeed REST API at:

    http://0.0.0.0:8888/test/users


## Development

If you want to update your image with the latest versions from master, these work (but I am still looking for a better solution)

    docker build -t backfeed-restapi-service --no-cache=true .

Or login to the docker image:

    docker run -it backfeed-restapi-service /bin/bash 

and inside, run

    pip install -r requirements.txt -U