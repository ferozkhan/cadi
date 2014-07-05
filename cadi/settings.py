"""
Django settings for cadi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x@m91o2tavcl!+z^3-n@&5_^=^u7znh^@_ncu1q$b-@0l8todu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Allow all host headers
ALLOWED_HOSTS = ['*']

# Application definition
ROOT_URLCONF = 'cadi.urls'

INSTALLED_APPS=(
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES=(
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_DIRS=(
    os.path.join(BASE_DIR, 'templates')
)

STATIC_URL = '/static/'


WSGI_APPLICATION = 'cadi.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
