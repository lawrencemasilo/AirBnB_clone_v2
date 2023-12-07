#!/usr/bin/python3
"""a module that distributes an archive to my web servers,
using the function do_deploy"""
from fabric.api import env, put, run
import os
import sys

web_01 = '18.207.142.181'
web_02 = '100.25.38.166'
env.hosts = [web_01, web_02]
env.user = sys.argv[-1]
env.key_filename = sys.argv[-2]


def do_deploy(archive_path):
    """
    returns True when deployed successfully, or False
    """

    if os.path.exists(archive_path) is False:
        return False

    try:
        file_name = archive_path.split('/')[-1]
        directory = file_name.replace('.tgz', '')

        put(archive_path, '/tmp/')
        run(f'mkdir -p /data/web_static/releases/{directory}/')
        run(f"""tar -xzf /tmp/{file_name} -C
                /data/web_static/releases/{directory}/""")
        run(f'rm /tmp/{file_name}')
        run(f"""mv /data/web_static/releases/{directory}/web_static/*
                /data/web_static/releases/{directory}/""")
        run(f'rm -rf /data/web_static/releases/{directory}/web_static')
        run('rm -rf /data/web_static/current')
        run(f"""ln -s /data/web_static/releases/{directory}/
                /data/web_static/current""")
        print("New version deployed!")
        return True
    except Exception:
        return False
