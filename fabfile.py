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
evn.repo_url = ''

"""
Environments
"""


def staging(web_ip, mongo_ips):

    env.web_ip = web_ip
    env.mongo_ips = mongo_ips

    env.settings = 'staging'
    env.hosts = ['%s:22' % web_ip]
    env.user = 'djages'

def setup(ip, username, password=None, port=22)
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

def new_user(username, password):   
    
    runcmd('adduser {username} --disabled-password --gecos ""'.format(
        username=username))
    runcmd('adduser {username} sudo'.format(
        username=username))
    
    runcmd('echo "{username}:{password}" | chpasswd'.format(
        username=username,
        password=password))

def install_packages():
    command = 'apt-get install python-software-properties python g++ make git python-pip python-virtualenv python-imaging build-essential python-dev libxml2-dev libxslt-dev python-lxml libssl-dev libpam0g-dev nginx apache2'
    runcmd(command)

def create_env(user):
    sudo('mkdir -p %(repo_path)s' % env)

    with prefix('cd %(repo_path)s' % env):
        run('git clone %(repo_url)s' % env)

    sudo('chown %s:%s %s' % (user, user, env.repo_path))


def ubuntu_init(new_username, new_password):
    install_packages()
    new_user(new_username, new_password)
    create_env(new_username)

"""
Commands - deployment
"""

def deploy_staging():
    print green("Performing a deployment to: %s" % env.hosts[0])
    checkout_latest()
    command = '%(repo_path)s/djages/scripts/deploy.sh --web_ip %(web_ip)s --mongo_ips %(mongo_ips)s' % env
            
    sudo(command, user='djages')


