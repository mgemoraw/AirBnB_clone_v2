#!/usr/bin/python3
from fabric.api import local
from time import strftime
from datetime import date


# a Fabric script that generates a .tgz archive
# from the contents of the web_static folder of
# your AirBnB Clone repo, using the function do_pack.
def do_pack():
    """ A script that generates archive the contents of web_static folder"""

    filename = strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
