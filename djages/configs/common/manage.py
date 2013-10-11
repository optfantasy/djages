#!/usr/bin/env python

import os
import sys

from django.core.management import execute_manager

# root of project directory
python_path = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), '../../../'
)
# local apps directory
apps_path = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), '../../apps'
)
# libs
lib_path = os.path.join(
    os.path.realpath(os.path.dirname(__file__)), '../../lib'
)

# we add them first to avoid any collisions
sys.path.insert(0, python_path)
sys.path.insert(0, apps_path)
sys.path.insert(0, lib_path)

import imp
try:
    imp.find_module('settings') # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n" % __file__)
    sys.exit(1)

import settings

if __name__ == "__main__":
    execute_manager(settings)
