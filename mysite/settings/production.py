
import os
from django.conf import settings

DEBUG = True
TEMPLATE_DEBUG = False
DATABASES = settings.DATABASES




# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()





# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

AWS_STORAGE_BUCKET_NAME = 'postart-main'
AWS_ACCESS_KEY_ID ='AKIAJYOI2ZJK4ADBSUGGA'
AWS_SECRET_ACCESS_KEY='vdTOjntz+nDF51h/eCSB7zc/Pg+mIA9wKjbwiQHm'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_HOST = 's3-us-west-2.amazonaws.com'
# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
STATIC_ROOT = 'staticfiles'
#STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
