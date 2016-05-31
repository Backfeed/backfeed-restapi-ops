import os
from datetime import datetime
import requests
import time
import types

from fabric.decorators import task
from fabric.api import local, cd, run, puts, settings, lcd, env

import logging
logging.basicConfig()
this_dir = os.path.dirname(__file__)


CONFIG = {
    'staging': {
        'host_string': 'backfeed@dmagbeta.backfeed.cc',  # dmagbeta -
        'sudo_host_string': 'dmagbeta.backfeed.cc',  # dmagbeta -
        'docker_image': 'backfeed-api',
        'installation_dir': '/home/backfeed/ops',
        'docker_compose_file': 'docker-compose-staging.yml',
        'docker_containers': [
            {
                'name': 'backfeed-api-ore',
                'port': '8889',
                'data_dir': '/home/backfeed/data-ore',
                'url': 'http://api-ore.staging.backfeed.cc',
            },
            {
                'name': 'backfeed-api',
                'port': '8888',
                'data_dir': '/home/backfeed/data',
                'url': 'http://api.staging.backfeed.cc',
            },
        ]
    },
    'production': {
        'host_string': 'backfeed@192.241.178.73',
        'installation_dir': '/home/backfeed/ops',
        'docker_compose_file': 'docker-compose-production.yml',
        'docker_containers': [
            {
                'name': 'backfeed-api',
                'port': '8888',
                'data_dir': '/home/backfeed/data',
                'url': 'http://api.staging.backfeed.cc',
            },
        ]
    }
}


@task
def build(where):
    """this will rebuild the docker file"""
    print '*** THIS WILL RESTART THE SERVICE ***'
    config = get_config(where)
    with settings(host_string=config['host_string']), cd(config['installation_dir']):
        run('git pull')
        run('docker-compose -f {docker_compose_file} build'.format(**config))
        run('docker-compose -f {docker_compose_file} up'.format(**config))
    livetest(where)


@task
def restart(where):
    config = get_config(where)
    with settings(host_string=config['host_string']), cd(config['installation_dir']):
        cmd = 'docker-compose -f {docker_compose_file} restart'.format(**config)
        run(cmd)


@task
def update(where):
    """this will update the python packages in the docker file"""
    config = get_config(where)
    with settings(host_string=config['host_string']), cd(config['installation_dir']):
        for container in config['docker_containers']:
            cmd = 'docker-compose -f {docker_compose_file} exec {container} update'.format(container=container['name'], **config)
            run(cmd)
            cmd = 'docker-compose -f {docker_compose_file} exec {container} sv hup backfeed'.format(container=container['name'], **config)
            run(cmd)
    livetest(where)


@task
def livetest(where):
    """just test if the thing is up"""
    config = get_config(where)
    for container in config['docker_containers']:
        url = container['url'] + '/example/users'
        print 'getting', url
        response = requests.get(url)
        print response


class Config(dict):
    def __init__(self, **kwargs):
        for k in kwargs:
            if isinstance(kwargs[k], types.ListType):
                self[k] = []
                for v in kwargs[k]:
                    if isinstance(v, types.DictType):
                        self[k].append(Config(**v))

                    else:
                        self[k].append(v) 
            elif isinstance(kwargs[k], types.DictType):
                self[k] = Config(**kwargs[k])
            else:
                self[k] = kwargs[k]
        for k in self:
            setattr(self, k, self[k])


def get_config(where):
    if where not in CONFIG:
        print 'Possible values are:'
        for key in CONFIG:
            print '\t - {key}'.format(**locals())
        print '-' * 30
        raise Exception('There is no configuration for "{where}"'.format(**locals()))
    config = Config(**CONFIG[where])
    return config

@task
def setup_database(where):
    config = get_config(where)
    with settings(host_string=config['host_string']), cd(config['installation_dir']):
        container = {
            'name': 'backfeed-postgres', 
        }

        run('docker-compose exec {name} su postgres -c "createuser backfeed -SDRP"'.format(**container))
        run('docker-compose exec {name} su postgres -c "createdb backfeed --owner=backfeed"'.format(**container))
