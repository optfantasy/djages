import json
import urllib
import urllib2

from fabric.api import *
from fabric.operations import *
from fabric.utils import *
from fabric.contrib.files import *
from fabric.colors import green, yellow, red

"""
Base configuration
"""
env.project_name = 'djages'
env.path = '/home/djages/site/%(project_name)s' % env
env.repo_path = '%(path)s/repository' % env
env.env_path = '%(path)s/env' % env
env.repo_url = 'https://github.com/optfantasy/djages'

"""
Environments
"""


def staging(web_ip, mongo_ips):

    env.web_ip = web_ip
    env.mongo_ips = mongo_ips

    env.settings = 'staging'
    env.hosts = ['%s:22' % web_ip]
    env.user = 'djages'

def setup(ip, username, password=None, port=22):
    env.hosts = ['%s:%s' % (ip, port)]
    env.user = username
    if password:
        env.password = password

"""
Branches
"""
def branch(branch_name):
    """
    Selects any an arbitrary branch.
    """
    env.branch = branch_name


def checkout_latest():
    """
    Pull the latest code on the specified branch.  Overwrites any local
    configuration changes.
    """
    print yellow("Pulling latest source...")

    with prefix('cd %(repo_path)s' % env):
        #sudo('chown -R %(user)s %(path)s' % env)
        run('git reset --hard HEAD')
        run('git checkout %(branch)s' % env)
        run('git pull origin %(branch)s' % env)

"""
Commands - setup
"""

def new_user(username, public_key_path):

    if not exists('/home/%s' % username):

        run('sudo adduser {username} --disabled-password --gecos ""'.format(
            username=username))
        run('sudo adduser {username} sudo'.format(
            username=username))
        run('echo "%s ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers' % username)

        f = file(public_key_path)
        key = f.read()

        if not exists('/home/%s/.ssh' % username):
            run('sudo mkdir -p /home/%s/.ssh' % username)
            run('sudo chown -R %(name)s:%(name)s /home/%(name)s/.ssh' % {'name':username})

            run('echo "%s" | sudo tee -a /home/%s/.ssh/authorized_keys' % (key, username))
            run('sudo chown %(name)s:%(name)s /home/%(name)s/.ssh/authorized_keys' % {'name':username})
            run('sudo chmod 600 /home/%(name)s/.ssh/authorized_keys' % {'name':username})
        f.close()


def install_packages():
    command = 'sudo apt-get update;sudo apt-get -y install python-software-properties python g++ make git python-pip python-virtualenv python-imaging build-essential python-dev libxml2-dev libxslt-dev python-lxml libssl-dev libpam0g-dev nginx apache2 libapache2-mod-wsgi'
    run(command)
    if exists('/etc/nginx/sites-enabled/default'):
        run('sudo rm -r /etc/nginx/sites-enabled/default')
    if exists('/etc/apache2/sites-enabled/000-default.conf'):
        run('sudo rm -r /etc/apache2/sites-enabled/000-default.conf')
    if exists('/etc/apache2/sites-enabled/000-default'):
        run('sudo rm -r /etc/apache2/sites-enabled/000-default')

    run('sudo a2enmod headers')
    run('sudo a2enmod expires')


def install_mongodb():
    command = 'wget https://raw.github.com/gage/server_scripts/master/mongodb_install.sh -v -O mongodb_install.sh;chmod +x ./mongodb_install.sh;./mongodb_install.sh; rm -rf mongodb_install.sh'
    with prefix('cd /tmp'):
        run(command)

def create_env():
    if not exists('%(path)s' % env):
        run('sudo mkdir -p %(path)s' % env)
        run('sudo mkdir -p /home/%(project_name)s/logs' % env)
        run('sudo chown -R %(project_name)s:%(project_name)s /home/%(project_name)s/site' % env)

def create_repo():
    env.user = env.project_name
    if not exists('%(repo_path)s' % env):
        with prefix('cd %(path)s' % env):
            run('git clone %s repository' % env.repo_url)
    if not exists('%(repo_path)s/%(project_name)s/configs/common/jinja_cache' % env):
        run('mkdir -p %(repo_path)s/%(project_name)s/configs/common/jinja_cache' % env)
    run('sudo chown -R www-data:www-data %(repo_path)s/%(project_name)s/configs/common/jinja_cache' % env)
    if not exists('%(repo_path)s/%(project_name)s/configs/staging/jinja_cache' % env):
        run('mkdir -p %(repo_path)s/%(project_name)s/configs/staging/jinja_cache' % env)
    run('sudo chown -R www-data:www-data %(repo_path)s/%(project_name)s/configs/staging/jinja_cache' % env)

def setup_vitrualenv():
    env.user = env.project_name
    if not exists('%(env_path)s' % env):
        with prefix('cd %(path)s' % env):
            run('virtualenv env' % env)
    with prefix('cd %(repo_path)s' % env):
        with prefix('source %(env_path)s/bin/activate' % env):
            run('pip install -r requirements.txt')

def ubuntu_init(public_key_path):
    install_packages()
    install_mongodb()
    new_user(env.project_name, public_key_path)
    create_env()
    create_repo()
    setup_vitrualenv()

"""
Commands - deployment
"""

def deploy_staging():
    print green("Performing a deployment to: %s" % env.hosts[0])
    checkout_latest()
    command = '%(repo_path)s/djages/scripts/deploy.sh --web_ip %(web_ip)s --mongo_ips %(mongo_ips)s' % env
            
    sudo(command, user='djages')


