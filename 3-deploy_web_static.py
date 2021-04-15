#!/usr/bin/python3
"""
    Fabric script to automate deployment of web_static directory
"""
from fabric.api import run, put, local, env
from datetime import datetime
import os.path


env.hosts = ['34.73.100.0', '34.228.167.237']


def do_pack():
    """
     generates a .tgz archive from the contents of the web_static folder of
     your AirBnB Clone repo, using the function do_pack.
    """
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = 'versions/web_static_' + date + '.tgz'
    if not (os.path.exists("versions")):
        local('mkdir -p versions')
    local('tar -cvzf ' + path + ' web_static')
    if (os.path.exists(path)):
        return path
    return None


def do_deploy(archive_path):
    """
    - Upload the archive to the /tmp/ directory of the web server
    - iUncompress the archive to the folder /data/web_static/releases/<archive
    filename without extension> on the web server
    - Delete the archive from the web server
    - Delete the symbolic link /data/web_static/current from the web server
    - Create a new the symbolic link /data/web_static/current on the web
    server, linked to the new version of your code
    (/data/web_static/releases/<archive filename without extension>)
    """
    if not (os.path.exists(archive_path)):
            return False
    archive_name = archive_path.split('/')[1]
    archive_name_without_ext = archive_path.split('/')[1].split('.')[0]
    release_path = '/data/web_static/releases/' + archive_name_without_ext
    upload_path = '/tmp/' + archive_name
    put(archive_path, upload_path)
    run('mkdir -p ' + release_path)
    run('tar -xzf ' + upload_path + ' -C ' + release_path)
    run('rm ' + upload_path)
    run('mv ' + release_path + '/web_static/* ' + release_path + '/')
    run('rm -rf ' + release_path + '/web_static')
    run('rm -rf /data/web_static/current')
    run('ln -s ' + release_path + ' /data/web_static/current')
    return True


def deploy():
    """
    - Call the do_pack() function and store the path of the created archive
    - Return False if no archive has been created
    - Call the do_deploy(archive_path) function, using the new path of the new
      archive
    - Return the return value of do_deploy
    """
    path = do_pack()
    if (path is None):
        return False
    deploy = do_deploy(path)
    if (deploy is False):
        return False
    return deploy
