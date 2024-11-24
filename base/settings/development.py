from .authentication import *
from .configuration import *

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SECRET_KEY = "$45*gq_fug9o(71of_)n!v*&ca%jw!cuzbiq_^o9*05sd8)95("
