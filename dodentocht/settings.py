"""
Django settings for dodentocht project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

if DEBUG:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/
    STATIC_PATH = os.path.join(BASE_DIR, 'static')

    # Define STATIC_ROOT for apps that compress all static files into 1
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    STATIC_URL = '/static/'

    STATICFILES_DIRS = [
        STATIC_PATH,
        ]

    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases

    DATABASES = {
        'default': {
            'NAME': 'dodentocht',
            'ENGINE': 'mysql.connector.django',
            'USER': 'root',
            'PASSWORD': 'Will0870',
            'HOST': 'EXERGOS-PC',
            'OPTIONS': {
              'autocommit': True,
            },
        }
    }

else:
    # HEROKU PRODUCTION
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/

    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    # Production database
    CLEARDB_DATABASE_URL = "mysql://b21ac369402104:71a611ed@us-cdbr-iron-east-01.cleardb.net/heroku_a8c4b0cefde9e4f"

    DATABASES = {
        'default': {
            'NAME': 'heroku_a8c4b0cefde9e4f',
            'ENGINE': 'mysql.connector.django',
            'USER': 'b21ac369402104',
            'PASSWORD': '71a611ed',
            'HOST': 'us-cdbr-iron-east-01.cleardb.net',
            # 'PORT' : '3306',
            'OPTIONS': {
                'autocommit': True,
                'connect_timeout': 20000,
                },
            }
    }

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-(b79id^=!!x&!7x6ld3798+e5r6ny60o$_6lg3^i9q&)x+&8)'



TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_dodentocht',

    # other apps
    "compressor",

    # gunicorn, for heroku deployment
    "gunicorn",

    # for amazon AWS connection
    "storages",
    "boto",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dodentocht.urls'

WSGI_APPLICATION = 'dodentocht.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')
TEMPLATE_DIRS = [
    TEMPLATE_PATH,
    ]

# Include sass
COMPRESS_PRECOMPILERS = (
    ('text/scss', 'sass --scss {infile} {outfile}'),
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

STATICFILES_FINDERS = (
    # other finders..
    # 'compressor.finders.CompressorFinder',
)



# # In production
# #Storage on S3 settings are stored as os.environs to keep settings.py clean
# # ENVIRONMENT VARIABLES ARE DECLARED IN HEROKU SHELL
# # heroku config:add AWS_ACCESS_KEY_ID=youraswsaccesskey
# # heroku config:add AWS_SECRET_ACCESS_KEY=yourawssecretkey
# # heroku config:add S3_BUCKET_NAME=yourbucketname
#
# # if not DEBUG:
# S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
# AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
# AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# S3_URL = 'http://%s.s3.amazonaws.com/' % S3_BUCKET_NAME
# STATIC_URL = S3_URL