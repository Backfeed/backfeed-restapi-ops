**this is sort of semi-confidential - and is why this repo is private**


# What is where

## api.staging.backfeed.cc

    159.203.172.115
    running on port 8888.

data directory:

    /home/backfeed/data 

nginx config:

    /etc/nginx/sites-available/api.staging.backfeed.cc

start with 

    docker run -dit -p 8888:8888 -v /home/backfeed/data:/data backfeed-api


## api-ore.staging.backfeed.cc

    159.203.172.115
    running on port 8888.

data directory:

    /home/backfeed/data-ore

nginx config:

    /etc/nginx/sites-available/api-ore.staging.backfeed.cc
start with 

    docker run -dit -p 8889:8888 -v /home/backfeed/data-ore:/data backfeed-api
