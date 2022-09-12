import os
from pathlib import Path

from dotenv import dotenv_values

BASE_DIR = Path(__file__).resolve().parent.parent
config = dotenv_values(".env")

DEBUG = True

HOST_NAME = config['HOST']
BASE_URL = config['BASE_URL']
BOT_TOKEN = config['BOT_TOKEN']
CHANNEL_ID = config['CHANNEL_ID']

CSRF_TRUSTED_ORIGINS = [
    HOST_NAME,
    BASE_URL
]

CORS_ORIGIN_WHITELIST = [
    HOST_NAME,
    BASE_URL
]

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django_json_widget',
    'django.contrib.admin',
    'exchange_rate'
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
]

ROOT_URLCONF = 'crm.urls'

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

WSGI_APPLICATION = 'crm.wsgi.application'

DATABASES = {
    "default": {
        "ENGINE": config.get('DB_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': config.get('POSTGRES_DB', 'postgres'),
        'USER': config.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': config.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': config.get('DB_HOST', 'db'),
        'PORT': config.get('PORT', '5432'),
    }
}

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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config['DSN_REDIS'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}
