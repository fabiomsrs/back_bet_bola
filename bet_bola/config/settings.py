"""
Django settings for bet_bola project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
#import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 't9xein@q$yf$w+ks2m&hr&53j1n@rtyg7o(b1(-)ffz7nce-kg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']
DB_SWAP_LOCAL = True



APP_VERBOSE_NAME = 'sitename'
# Application definition

INSTALLED_APPS = [
    'config.apps.MyAdminConfig',    
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'corsheaders',    
    'rest_framework',
    'filters',
    'core',
    'user',
    'history',
    'utils',
    'updater',
    'ticket'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 9999999

AUTH_USER_MODEL = 'user.CustomUser'

ROOT_URLCONF = 'config.urls'

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
                'django.template.context_processors.i18n',
            ],
        },
    },
]


WSGI_APPLICATION = 'config.wsgi.application'


# STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

if DB_SWAP_LOCAL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'bet_bola_api',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'localhost',
            'PORT': '5432',
            'CHARSET':'UTF8'
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'db_sitename',
            'USER': 'user_sitename',
            'PASSWORD': 'db_password',
            'HOST': 'localhost',
            'PORT': '5432',
            'CHARSET':'UTF8'
        }
    }


ADMINS = [('pablo', 'pabllobeg@gmail.com'),]

#Logging
LOG_ALL_ERRORS_DEFAULT = True
if LOG_ALL_ERRORS_DEFAULT:
    LOGGING = {
    'version':1,
    'disable_existing_loggers': False,
    'formatters':{
        'large':{
            'format':'%(asctime)s  %(levelname)s  %(process)d  %(pathname)s  %(funcName)s  %(lineno)d  %(message)s  '
        },
        'tiny':{
            'format':'%(asctime)s  %(message)s  '
        }
    },
    'handlers':{        
        'debug_file':{
            'level':'INFO',
            'class': 'logging.FileHandler',            
            'filename':'logs/DebugLoggers.log',
            'formatter':'large',
        },
    },
    'loggers':{        
        'debug_logger':{
            'handlers':['debug_file'],
            'level':'DEBUG',
            'propagate':True,
        },
    },
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

from django.utils.translation import gettext_lazy as _

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

LANGUAGES = (
    ('en', _('Inglês')),
    ('pt-br', _('Português'))
)

LANGUAGE_CODE = 'pt-br'

#Decimal
DECIMAL_SEPARATOR = '.'
#USE_THOUSAND_SEPARATOR = True

#Encoding
DEFAULT_CHARSET = 'utf-8'

#Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'betemailsender@gmail.com'
EMAIL_HOST_PASSWORD = 'plataformabet'
EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'Pablo <noreply@example.com>'

#Zones
TIME_ZONE = 'UTC'
TIME_ZONE_LOCAL = 'America/Sao_Paulo'

USE_I18N = True
USE_L10N = True
USE_TZ = False


#Statis Files
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = '/home/mushzinho5/webapps/static_sitename'
STATIC_URL = '/static/'
STATICFILES_IRSD = [
    os.path.join(BASE_DIR, "static")
]

REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%d %B %Y %H:%M",
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),    
    'DEFAULT_AUTHENTICATION_CLASSES': (        
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication'
    )
}


CORS_ORIGIN_ALLOW_ALL = True