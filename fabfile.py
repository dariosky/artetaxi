import os

from fabric.context_managers import cd
from fabric.decorators import task
from fabric.operations import run
from fabric.state import env

if os.path.exists(os.path.expanduser("~/.ssh/config")):
    env.use_ssh_config = True

WEBAPP_FOLDER = '~/apps/artetaxi'
env.hosts = 'opal'


@task
def deploy():
    with cd(WEBAPP_FOLDER):
        run('git pull')
