from .base import *

from django.contrib.messages import constants as messages

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LANGUAGE_CODE = "en-IN"

LOGIN_REDIRECT_URL = "/"

LOGIN_URL = "/"

LOGOUT_REDIRECT_URL = "/"

LOGOUT_URL = "/"

MEDIA_ROOT = BASE_DIR / "media"

MEDIA_URL = "media/"

MESSAGE_TAGS = {
    messages.DEBUG: "DEBUG",
    messages.ERROR: "ERROR",
    messages.INFO: "INFO",
    messages.SUCCESS: "SUCCESS",
    messages.WARNING: "WARNING",
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}


SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_COOKIE_AGE = 240 * 60

SESSION_IDLE_TIMEOUT = 240 * 60

SITE_ID = 1

STATIC_URL = "static/"

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True

USE_TZ = True
