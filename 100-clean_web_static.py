#!/usr/bin/python3
"""
    Fabric script to automate deployment of web_static directory
"""
from fabric.api import run, put, local, env, execute, hosts
from datetime import datetime
import os.path


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


@hosts('35.227.3.110', '35.227.20.183')
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
    path = execute(do_pack)
    if (path is None):
        return False
    deploy = execute(do_deploy, archive_path=path['<local-only>'])
    if (deploy is False):
        return False
    return deploy


def do_stress():
    """
    Function made for debugging purpose of fn do_clean
    """
    for i in range(0, 10):
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        path = 'versions/web_static_' + date + "_" + str(i) + '.tgz'
        local('touch ' + path)


@hosts('35.227.3.110', '35.227.20.183')
def do_clean(number=0):
    """
    deletes out-of-date archives.
    Return True if there is not operation to do otherwise False if an error is
    raised
    """
    try:
        number = int(number)
    except Exception:
        return False
    archives_nb = local('ls -ltr versions | wc -l', capture=True).stdout
    archives_nb = int(archives_nb) - 1
    if (archives_nb <= 0 or archives_nb == 1):
        return True
    if (number == 0 or number == 1):
        remove_nb = archives_nb - 1
    else:
        remove_nb = archives_nb - number
        if (remove_nb <= 0):
            return True
    archives_list = local("ls -ltr versions | tail -n " + str(archives_nb) + "\
            | head -n \
            " + str(remove_nb) + "\
            | awk '{print $9}'", capture=True).rsplit("\n")
    if len(archives_list) >= 1:
        for archive_name in archives_list:
            if (archive_name != ''):
                local('rm versions/' + archive_name)
                run('rm -rf /data/web_static/releases/\
                    ' + archive_name.split('.')[0])
