"""
Django settings for emergency project.

Generated by 'django-admin startproject' using Django 2.20.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0.0/g/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0.0/g/ref/settings/
"""

import os
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Added because https://docs.djangoproject.com/en/2.0/ref/contrib/flatpages/
SITE_ID = 1

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!!!!!!!!move me to .env file!!!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# GEODJANGO settings
# Required for HEROKU
GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')


# Application definition


DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # added, but not a django default
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.gis',
]
LOCAL_APPS = [
    'maps.apps.MapsConfig',
]

THIRD_PARTY_APPS = [
    'django_countries',
]


INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'emergency.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'emergency.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'nomad_emergency',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

# THE HEROKU PART
# TODO: strip out and just use dj_database_url
django_heroku.settings(locals())

# Fix Database Engine because djanog_heroku is being dumb
# https://github.com/heroku/django-heroku/issues/6
if os.getenv('DATABASE_URL'):
    if DATABASES['default']['ENGINE'] in ('django.db.backends.postgresql', 'django.db.backends.postgresql_psycopg2'):
        DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
    elif DATABASES['default']['ENGINE'] == 'django.db.backends.sqlite3':
        DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.spatialite'