from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7+r$x_+l6^(*o(3w1l4y!z)2p83dn&b5fm!5o8k25m852_-0z6"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = INSTALLED_APPS + [
    "django_browser_reload",
    "debug_toolbar",
]

MIDDLEWARE = MIDDLEWARE + [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ==============
# STATIC
# ==============

STATICFILE_PATH = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    "static",
]

STATIC_ROOT = os.path.join(BASE_DIR, "raw-template-static")
STATIC_URL = "/raw-template-static/"


MEDIA_ROOT = os.path.join(BASE_DIR, "raw-template-media")
MEDIA_URL = "/raw-template-media/"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": os.path.join("log/output.log"),
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}


INTERNAL_IPS = [
    "127.0.0.1",
]

try:
    from .local import *
except ImportError:
    pass
