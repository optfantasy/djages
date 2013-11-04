### Djages = Django + Mongodb + RESTful API
Djages is an app base on [django-nonrel](https://github.com/django-nonrel/django) and [mongodb-engine](https://github.com/django-nonrel/mongodb-engine). You can easily create a web app with power of Django, Mongodb and a RESTful API framework.

#### Requirement
For Djages, all you need is python and a virtual environment. 
On Mac, you can follow this [post](http://www.thisisthegreenroom.com/2011/installing-python-numpy-scipy-matplotlib-and-ipython-on-lion/#python).
On Ubuntu, you can just do

````bash
$ sudo apt-get install python-software-properties python g++ make git python-pip python-virtualenv python-imaging build-essential python-dev libxml2-dev libxslt-dev python-lxml libssl-dev libpam0g-dev nginx apache2
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

#### Get Start
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

#### Contributors
* [Gage Tseng](https://github.com/gage/)
* [Sean Cheng](https://github.com/sainteye/)
* [Jadon ke](https://github.com/jasonke/)
* [Redbug](https://github.com/redbug/)
