from djages.configs.common.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MEDIA_URL = 'http://web_ip/'


ADMIN_MEDIA_PREFIX = '/static/admin/'
DOWNLOAD_DIRECTORY = '/tmp/'

### Mobile Session Checking
MOBILE_CHECK_SESSION = True

# Predefined domain
SITE_DOMAIN = 'web_ip'
SITE_ID = '50b3b56c9f44722b5a000024'
#SITE_PORT = "80"

## DB
DATABASES = {
    'default': {
    	'ENGINE': 'dbindexer',
    	'TARGET': 'mongodb',
        'NAME': 'djages',
        'TEST_NAME': 'test_djages',
        'HOST': 'localhost',
    },
    'mongodb': {
    	'ENGINE': 'django_mongodb_engine',
    	'NAME': 'djages',
    	'TEST_NAME': 'test_djages',
        'HOST': 'localhost',
    },
}

# Internal IPs for security
INTERNAL_IPS = ()


