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
DEBUG = True

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

    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

    TEMPLATE_DIRS = [
        TEMPLATE_PATH,
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

    STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    )

    # Include sass
    COMPRESS_PRECOMPILERS = (
        ('text/scss', 'sass --scss {infile} {outfile}'),
        ('text/x-scss', 'django_libsass.SassCompiler'),
    )

    ALLOWED_HOSTS = []

else:
    # HEROKU PRODUCTION
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # If collectstatic is used when uploading to heroku, use staticfiles root
    STATIC_ROOT = 'staticfiles'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
        os.path.join(os.path.dirname(BASE_DIR), 'static'),
    )
    # Simplified static file serving.
    # https://warehouse.python.org/project/whitenoise/

    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    TEMPLATE_PATH = os.path.join(os.path.dirname(BASE_DIR), 'templates')

    TEMPLATE_DIRS = [
        TEMPLATE_PATH,
        ]

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

    STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    # Allow all host headers
    ALLOWED_HOSTS = ['*']


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-(b79id^=!!x&!7x6ld3798+e5r6ny60o$_6lg3^i9q&)x+&8)'



TEMPLATE_DEBUG = True

# If DEBUG is true, use sass, else, in production, use standard css
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'app_dodentocht.context_processors.debug',
)



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
    # compressor for sass
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
    # SessionAuthenticationMiddleware does not exist in django 1.6.10
    # ==> when using it, comment next line
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