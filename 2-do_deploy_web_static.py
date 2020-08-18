#!/usr/bin/python3
""" Compress web_static """
import os
from datetime import datetime
from fabric.api import local, put, env, run

env.hosts = ['34.75.211.75', '54.242.199.6']


def do_pack():
    """ Compresses web_static """
    if not os.path.isdir('versions'):
        os.mkdir('versions')
    time = datetime.now()
    name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(time.year, time.month,
                                                         time.day, time.hour,
                                                         time.minute,
                                                         time.second)
    if local('tar -cvzf {} web_static'.format(name)).succeeded:
        return name
    return None


def do_deploy(archive_path):
    """ Uploads an archive to remote server """
    if not os.path.isfile(archive_path):
        return False

    name = put(archive_path, '/tmp/')[0][5:-4]
    res = run('mkdir -p /data/web_static/releases/{}/'.format(name)).failed
    res = res or run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/\
'.format(name, name)).failed
    res = res or run('rm /tmp/{}.tgz'.format(name)).failed
    res = res or run('mv /data/web_static/releases/{}/web_static/* \
/data/web_static/releases/{}/'.format(name, name)).failed
    res = res or run('rm -rf /data/web_static/releases/{}/web_static\
'.format(name)).failed
    res = res or run('rm -rf /data/web_static/current').failed
    res = res or run('ln -s /data/web_static/releases/{}/ \
/data/web_static/current'.format(name)).failed

    if res:
        return False
    return True
