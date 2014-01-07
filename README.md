### Djages = Django + Mongodb + RESTful API
Djages is an app base on [django-nonrel](https://github.com/django-nonrel/django) and [mongodb-engine](https://github.com/django-nonrel/mongodb-engine). You can easily create a web app with power of Django, Mongodb and a RESTful API framework.

#### Requirement (for local dev)
For Djages, all you need is python and a virtual environment. 
On Mac, you can follow this [post](http://darklaunch.com/2011/11/24/osx-install-pip-virtualenv-virtualenvwrapper-on-mac).
and execute following command for PIL:
````bash
$ brew install libjpeg
````

On Ubuntu, you can just do

````bash
$ sudo apt-get install python-software-properties python g++ git make python-pip python-virtualenv python-imaging build-essential python-dev libxml2-dev libxslt-dev python-lxml libssl-dev libpam0g-dev nginx apache2 libapache2-mod-wsgi libgraphicsmagick++-dev libjpeg8-dev
````

For PIL in ubuntu, you may need to do this.
````bash
# sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
# sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
# sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
````

Create a virtual enviroment for Djages.

````bash
$ virtualenv djagesenv
````

and activate it

````bash
$ source ./djagesenv/bin/activate
````

or use mkvirtualenv if you have installed virtualenvwrapper

````bash
$ mkvirtualenv djagesenv
````

to deactivate virtualenv

````bash
$ deactivate
````

You may need to install [mongodb](http://www.mongodb.org/).
Tutorial: [OS X](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-os-x/), [Ubuntu](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/)

#### Getting Start (for local dev)
````bash
$ git clone https://github.com/optfantasy/djages
$ cd djages
$ pip install -r requirements.txt
$ ./startnewsite YOUR_APP_NAME
$ ./manage runserver
````

#### Create Superuser (for local dev)
````bash
$ ./manage createsuperuser
````

#### Setup Your Git Repository
Suppose you have a git repository: https://github.com/example/repository, with username git_user.

1) Edit fabile.py.
Change
````bash
env.repo_url = "https://github.com/optfantasy/djages"
````

to
````bash
env.repo_url = "https://git_user@github.com/example/repository"
````

2) Edit .git/config
Change
````bash
url = git@github.com:optfantasy/djages.git
````

to below if you use github:
````bash
url = git@github.com:example/repository.git
````

or this if you use bitbucket:
````bash
url = ssh://git@bitbucket.org/example/repository.git
````

3) Commit your change and push to git repository for next step.

#### Deploy to Ubuntu Server -- Setup
Suppose you have an ubuntu server with IP/domain example.com.

1) Edit file "deploy": change YOUR_SERVER_IP_OR_DOAMIN to "example.com" and MONGO_DB_IP to "localhost".

2) [Generate a SSH key pair](https://help.github.com/articles/generating-ssh-keys) for your remote user. Remember the public key path, it will be used in next step.
````bash
$ ssh-keygen -t rsa -C "your_email@example.com"
# Enter file in which to save the key (/Users/you/.ssh/id_rsa): YOUR_APP_NAME.pem [Press enter]
$ ssh-add YOUR_APP_NAME.pem
````
The file YOUR_APP_NAME.pem can be shared with your coworker, so that they can also deploy server.

3) Initialize site environment by given a username who has sudo permission and file path of public key.
````bash
$ ./deploy init USER_WITH_SUDO_PERMISSION PATH_OF_PUBLIC_KEY
````

If your server is in AWS ("ubuntu" is the user who has sudo permission), the initialize command will be like this:
````bash
$ ./deploy init ubuntu ~/.ssh/YOUR_APP_NAME.pem.pub
````

for Digital Ocean ("root" is the user who has sudo permission)
````bash
$ ./deploy init root ~/.ssh/YOUR_APP_NAME.pem.pub
````

#### Deploy to Ubuntu Server -- Deploy Project
Deploy your code to your ubuntu server.
````bash
$ ./deploy
````

After deploy, for ubuntu 13.10, you may need to edit /etc/apache2/apache.conf, comment out these lines
````bash
# <Directory /> 
#       Options FollowSymLinks 
# 		AllowOverride None 
# 		Require all denied 
# </Directory> 
# <Directory /usr/share> 
# 		AllowOverride None 
# 		Require all granted 
# </Directory> 
# <Directory /var/www/> 
# 		Options Indexes FollowSymLinks 
# 		AllowOverride None 
# 		Require all granted 
# </Directory> 
````
Then do this at remote
````bash
$ sudo service apache2 restart
````

Go to your IP/domain : http://example.com to check if it works.
(Don't forget to open 80 port in your security group if you are using AWS)

#### Create Remote Superuser
````bash
$ ./deploy createsuperuser
````

#### Contributors
* [Gage Tseng](https://github.com/gage/)
* [Sean Cheng](https://github.com/sainteye/)
* [Jadon ke](https://github.com/jasonke/)
* [Redbug](https://github.com/redbug/)
