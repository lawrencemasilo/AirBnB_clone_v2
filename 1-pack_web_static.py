#!/usr/bin/python3
"""This module generates a .tgz archive from the contents of the web_static"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    returns the archive if successful or None
    """

    if os.path.exists('versions') is False:
        local('mkdir -p versions')

    time = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}.tgz".format(time)

    if local("tar -czvf versions/{} web_static".format(file_name)):
        return "versions/{}".format(file_name)
    return None
