#!/usr/bin/python3
""" Compress web_static """
import os
from datetime import datetime
from fabric.api import local


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
