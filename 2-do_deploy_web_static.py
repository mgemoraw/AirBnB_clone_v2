#!/usr/bin/python3
"""Compresses web static package"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['54.146.92.103', '100.26.234.70']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """Deploying compressed web files to server and unziping"""
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive using put command
        put(archive_path, '/tmp/')

        # create target directory
        ts = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/\
            '.format(ts))

        # unzip archive and delte tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/releases/web_static_{}/'.format(ts, ts))

        # now remove
        run('sudo rm -rf /data/web_static/releases/web_static_{}/\
             web_static'.format(ts))

        # delte pre-existing symbolic link (soft link)
        run('sudo rm -rf /data/web_static/releases/web_static_{}/ \
            /data/web_static/current'.format(ts))

        # re-establish symbolic soft link
        run('sudo ln -sf /data/web_static/releases/web_static_{}/ \
            /data/web_static/current'.format(ts))

    except Exception as e:
        return False

    # returns true on success
    return True
