
import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = False
DATABASES = settings.DATABASES


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage' # to allow admin collectstatic to put files in bucket

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

DATABASE_ENGINE = 'sqlite 3'
DATABASE_NAME = 'aws.db'



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# AWS settings
ACCESS_KEY ='AKIAIL25OMLAD6FEOO6A'
SECRET_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'postart-main'


# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
