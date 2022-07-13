import environ

from .base import *
from django.core.exceptions import ImproperlyConfigured

env = environ.Env(
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# SECRET_KEY_VALUE = os.getenv("SECRET_KEY_VALUE","y04g(6v&((y$29nfs6*fjb5@+di7i*u2c*5vu&zml8fa@7y(^k")
SECRET_KEY = env("SECRET_KEY_VALUE")

HOST_NAME = env("HOST_NAME")

ALLOWED_HOSTS = [HOST_NAME]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]






DATABASE_PATH = env("DATABASE_PATH")

if not DATABASE_PATH:
    raise ImproperlyConfigured("DATABASE_PATH should not be empty")


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(DATABASE_PATH, "raw-template_production.db"),
    }
}


# PUBLIC_FILE_PATH = os.getenv("PUBLIC_STATIC_PATH", "")
PUBLIC_FILE_PATH = env("PUBLIC_STATIC_PATH")

if not PUBLIC_FILE_PATH:
    raise ImproperlyConfigured("PUBLIC_FILE_PATH should not be empty")

# STATIC
STATIC_ROOT = os.path.join(PUBLIC_FILE_PATH, "raw-template-static")
STATIC_URL = "/raw-template-static/"
# MEDIA
MEDIA_ROOT = os.path.join(PUBLIC_FILE_PATH, "raw-template-media")
MEDIA_URL = "/raw-template-media/"

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



try:
    from .local import *
except ImportError:
    pass
