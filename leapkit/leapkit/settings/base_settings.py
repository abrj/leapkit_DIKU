"""
Django settings for leapkit project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from __future__ import absolute_import
import sys

from os.path import normpath, join
import os

import logging, logging.config

# #import dj_database_url

DEBUG = True

TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_FOLDER = os.path.join(os.path.dirname(__file__), "../..")

try:
    if sys.argv[1] == 'runserver' or sys.argv[1] == 'runserver_plus':
        DEBUG_TOOLBAR_PATCH_SETTINGS = DEBUG
    else:
        DEBUG_TOOLBAR_PATCH_SETTINGS = False
except IndexError:
    DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '93c=#%p9zz+_9fwakl3^(y%nex7$w9h-4=z11de@1x'

# SECURITY WARNING: don't run with debug turned on in production!


# ######### MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
    ('Anders Jorgensen', 'andersbrorup@gmail.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# ######### END MANAGER CONFIGURATION


ALLOWED_HOSTS = [
    'remote.leapkit.com',
    '127.0.0.1',
    'localhost',
    '*',
]


# Application definition

DJANGO_APPS = (
    'django_admin_bootstrapped.bootstrap3',
    'django_admin_bootstrapped',
    'autocomplete_light',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'root',
    'companies',
    'students',
    'institutions',
    'geographic_info',
    'projects',
    'queries',
)

THIRD_PARTY_APPS = (
    'south',
    'coverage',
    'selenium',
    'crispy_forms',
    'braces',
    'floppyforms',
    'static_precompiler',
    'rest_framework',
    'social_auth',
    'storages',
    'bootstrap_pagination',
    'opbeat.contrib.django',
    'debug_toolbar',
    # 'django-bootstrap-typeahead', - NOT USED
)

LAST_APPS = (
    'django_cleanup',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS + LAST_APPS

OPBEAT = {
    "ORGANIZATION_ID": "cdc57e5eb977499b8870bae933338a82",
    "APP_ID": "fb160ce6e7",
    "SECRET_TOKEN": "4f42bcdc2d9500748724acaadd198f9742c136db"
}

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
    'opbeat.contrib.django.middleware.Opbeat404CatchMiddleware',
)

ROOT_URLCONF = 'leapkit.urls'

WSGI_APPLICATION = 'leapkit.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'leapkit_db',
        'USER': 'leapkit_user',
        'PASSWORD': '12345q',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

TIME_ZONE = 'Europe/Copenhagen'

DATE_INPUT_FORMATS = ('%d/%m/%Y', '%Y/%m/%d')

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = (
    os.path.join(PROJECT_FOLDER, "static")
)

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'


USE_S3 = True
AWS_ACCESS_KEY_ID = 'AKIAJA5EKT7BXVYKYXIQ'
AWS_SECRET_ACCESS_KEY = '9bNYrT5ZT69BO3F/vTuPn9L86uaJa6Sg5uEQfYGT'
AWS_STORAGE_BUCKET_NAME = 'leapkitprofileimages'
AWS_QUERYSTRING_AUTH = False
S3_URL = 'https://%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

if USE_S3:
    DEFAULT_FILE_STORAGE = 'leapkit.s3utils.MediaRootS3BotoStorage'
    THUMBNAIL_DEFAULT_STORAGE = 'leapkit.s3utils.MediaRootS3BotoStorage'
    MEDIA_URL = S3_URL + '/media/'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_FOLDER, "media")



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Authentication
AUTHENTICATION_BACKENDS = ('social_auth.backends.contrib.linkedin.LinkedinBackend',
                           'django.contrib.auth.backends.ModelBackend',
)


# ######### TEMPLATE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'social_auth.context_processors.social_auth_by_name_backends',
    'social_auth.context_processors.social_auth_backends',
    'social_auth.context_processors.social_auth_by_type_backends',
    'social_auth.context_processors.social_auth_login_redirect',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    normpath(join(PROJECT_FOLDER, 'templates')),
)

# ######### END TEMPLATE CONFIGURATION



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
"""
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
"""

# Messages settings
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

CRISPY_TEMPLATE_PACK = 'bootstrap3'
CRISPY_FAIL_SILENTLY = False


# SSO setup
LINKEDIN_CONSUMER_KEY = '77bhjltt0kdchl'
LINKEDIN_CONSUMER_SECRET = 'ShHx5xlrAfG8vO1z'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/sign_in/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account-disconnected-redirect-url/'

SOCIAL_AUTH_COMPLETE_URL_NAME = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'

SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

SOCIAL_AUTH_UUID_LENGTH = 16

SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.associate.associate_by_email'
)

LOGIN_REDIRECT_URL = '/home/'
LOGIN_ERROR_URL = '/login_error/'

# EMAIL capabilities
EMAIL_HOST = 'leapkitcom.domain.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_USER = 'no_reply@leapkit.com'
EMAIL_HOST_PASSWORD = 'DjsjKA12'
DEFAULT_FROM_EMAIL = 'no_reply@leapkit.com'

DJANGO_LOG_LEVEL = DEBUG

# Loggin functionality
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['opbeat'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '[%(asctime)s] - %(levelname)s :  %(message)s'
        },
    },
    'handlers': {
        'opbeat': {
            'level': 'ERROR',
            'class': 'opbeat.contrib.django.handlers.OpbeatHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'debug_logger': {
            'level': 'DEBUG',
            'handlers': ['debug_handler'],
            'propagate': False
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'opbeat': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'opbeat.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


"""LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.__stdout__,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}"""

logging.config.dictConfig(LOGGING)
