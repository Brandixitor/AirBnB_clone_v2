#!/usr/bin/python3
"""
    Fabric script that generates a .tgz archive from the
    contents of the web_static folder of the AirBnB Clone repo.
"""
from os import makedirs
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Function that generates the archive. """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(timestamp)

    try:
        makedirs("./versions", exist_ok=True)
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path

    except:
        return None

