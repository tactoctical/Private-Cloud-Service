#!/usr/bin/python
import sys
import logging
import flask
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/tactocnet/")

from tactocnet import app as application
application.secret_key = 'roottactocstudios21035287'