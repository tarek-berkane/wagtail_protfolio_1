import environ

from .base import *
from django.core.exceptions import ImproperlyConfigured


config_file = "/home/coding43/config/portfolio"
env = environ.Env()
environ.Env.read_env(os.path.join(config_file, ".env"))


SECRET_KEY = env("SECRET_KEY")

HOST_NAME = env("HOST")

ALLOWED_HOSTS = [HOST_NAME]


# PUBLIC_FILE_PATH = os.getenv("PUBLIC_STATIC_PATH", "")
PUBLIC_DIR = env("PUBLIC_DIR")


# STATIC
STATIC_ROOT = os.path.join(PUBLIC_DIR, "raw-template-static")
STATIC_URL = "portfolio/raw-template-static/"
# MEDIA
MEDIA_ROOT = os.path.join(PUBLIC_DIR, "raw-template-media")
MEDIA_URL = "portfolio/raw-template-media/"

# SSL
SECURE_SSL_REDIRECT = True

# REDIS

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/production",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "verbose",
            "filename": os.path.join("log/output.log"),
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "WARNING"),
            "propagate": False,
        },
    },
}


# settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "read_default_file": os.path.join(config_file, "my.cnf"),
            "sql_mode": "traditional",
        },
    }
}
