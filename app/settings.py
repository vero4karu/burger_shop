"""
Django settings for a Burger Shop project.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'so-secret'

DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Applications
INSTALLED_APPS = (
    'app',
    'shop',
    'userprofile',

    'crispy_forms',
    'django_extensions',
    'grappelli',
    'pipeline',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'

WSGI_APPLICATION = 'app.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGIN_URL = 'userprofile:login'
LOGIN_REDIRECT_URL = 'home'

AUTH_USER_MODEL = 'userprofile.User'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'app', 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    
    'pipeline.finders.FileSystemFinder',
    'pipeline.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder',
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'

# django-crispy
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# django-grappelli
GRAPPELLI_ADMIN_TITLE = u'Burger Shop'

# django-pipeline
PIPELINE = {
    'PIPELINE_ENABLED': True,
    'JAVASCRIPT': {
        'main_js': {
            'source_filenames': (
                'js/order_form.js',
            ),
            'output_filename': 'js/main.min.js',
        }
    },
    'STYLESHEETS': {
        'global_css': {
            'source_filenames': (
                'css/styles.css',
            ),
            'output_filename': 'css/styles.min.css',
        }
    },
    'JS_COMPRESSOR': 'pipeline.compressors.jsmin.JSMinCompressor',
}


import sys
if 'test' in sys.argv:
    from app.test_settings import *
else:
    from app.local_settings import *

PIPELINE['PIPELINE_ENABLED'] = not DEBUG