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

    docker build -t backfeed-api .

Now start the docker image.

You need to tall the docker image (1) which port to listen on and (2) which data directory to use. For example, if you want the service to be available on port 8880, and save the data in ./backfeed-data-dir, you would start the service like tis:

    docker run -itd -p 8880:8888 -v ./backfeed-data-dir:data backfeed-api

You can then visit your Backfeed REST API at:

    http://0.0.0.0:8880/test/users


## Development

If you want to update your image with the latest versions from master, these work: 

    docker run -it backfeed-api update

You can also login to the docker instance:

    docker run -it backfeed-api /bin/bash 
