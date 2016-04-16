# Backfeed Protocol Service Ops

Stuff that has to do with deployment of the REST API

## Installation

Clone this repository and cd to the new :

    git clone ..
    cd newdir 

If you do not have docker installed, do that first:

    sudo apt-get install docker.io
    sudo service docker start

Build the docker image

    docker build -t backfeed-restapi-service .

Now start the docker image:

    docker run -it -p 8888 backfeed-restapi-service

You can then visit your Backfeed REST API at:

    http://0.0.0.0:8888/test/users


## Development

If you want to update your image with the latest versions from master:

    docker built -t backfeed-restapi-service  --no-cache=true