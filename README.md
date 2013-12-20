### Djages = Django + Mongodb + RESTful API
Djages is an app base on [django-nonrel](https://github.com/django-nonrel/django) and [mongodb-engine](https://github.com/django-nonrel/mongodb-engine). You can easily create a web app with power of Django, Mongodb and a RESTful API framework.

#### Requirement
For Djages, all you need is python and a virtual environment. 
On Mac, you can follow this [post](http://darklaunch.com/2011/11/24/osx-install-pip-virtualenv-virtualenvwrapper-on-mac).
On Ubuntu, you can just do

````bash
$ sudo apt-get install python-software-properties python g++ git make python-pip python-virtualenv python-imaging build-essential python-dev libxml2-dev libxslt-dev python-lxml libssl-dev libpam0g-dev nginx apache2 libapache2-mod-wsgi libgraphicsmagick++-dev
````

For PIL in ubuntu, you may need to do this.
````bash
# ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
# ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
# ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
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

#### Getting Start
````bash
$ git clone https://github.com/optfantasy/djages
$ cd djages
$ pip install -r requirements.txt
$ ./startnewsite YOUR_APP_NAME
$ ./manage runserver
````

#### Create Superuser
````bash
$ ./manage createsuperuser
````

#### Deploy to Ubuntu Server
Suppose you have an ubuntu server with IP/domain example.com.

1) Edit file "deploy": change YOUR_SERVER_IP_OR_DOAMIN to "example.com" and MONGO_DB_IP to "localhost".

2) [Generate a SSH key pair](https://help.github.com/articles/generating-ssh-keys) for your remote user. Remember the public key path, it will be used in next step.

3) Initialize site environment by given a username who has sudo permission and file path of public key.
````bash
$ ./deploy init USER_WITH_SUDO_PERMISSION PATH_OF_PUBLIC_KEY
````

If your server is in AWS ("ubuntu" is the user who has sudo permission), the initialize command will be like this:
````bash
$ ./deploy init ubuntu ~/.ssh/id_rsa.pub
````

Now, you can deploy your cade to your ubuntu server.
````bash
$ ./deploy
````

Go to your IP/domain : http://example.com to check if it works.
(Don't forget to open 80 port in your security group if you are using AWS)


#### Contributors
* [Gage Tseng](https://github.com/gage/)
* [Sean Cheng](https://github.com/sainteye/)
* [Jadon ke](https://github.com/jasonke/)
* [Redbug](https://github.com/redbug/)
