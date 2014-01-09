import copy
import datetime
import json
import re
import urllib, urllib2

from django.conf import settings

from BeautifulSoup import BeautifulSoup
from lxml import etree, html
from pyquery import PyQuery as pq
from urlparse import urlparse, parse_qs, parse_qsl
