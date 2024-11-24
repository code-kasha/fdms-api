ACCOUNT_ADAPTER = "allauth.account.adapter.DefaultAccountAdapter"

ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = True

ACCOUNT_AUTHENTICATION_METHOD = "username_email"

ACCOUNT_CHANGE_EMAIL = True

ACCOUNT_CONFIRM_EMAIL_ON_GET = False

ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "login"

ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = "/"

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_EMAIL_CONFIRMATION_HMAC = True

ACCOUNT_EMAIL_NOTIFICATIONS = False  # True - Debug

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_VERIFICATION = "optional"  # "mandatory", "optional", or "none".

ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = False

ACCOUNT_EMAIL_VERIFICATION_BY_CODE_MAX_ATTEMPTS = 3

ACCOUNT_EMAIL_VERIFICATION_BY_CODE_TIMEOUT = 900

ACCOUNT_EMAIL_SUBJECT_PREFIX = "[My Site]"

ACCOUNT_EMAIL_UNKNOWN_ACCOUNTS = True

ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"  # https

ACCOUNT_EMAIL_MAX_LENGTH = 254

ACCOUNT_MAX_EMAIL_ADDRESSES = None

ACCOUNT_FORMS = {
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "allauth.account.forms.ChangePasswordForm",
    "confirm_login_code": "allauth.account.forms.ConfirmLoginCodeForm",
    "login": "allauth.account.forms.LoginForm",
    "request_login_code": "allauth.account.forms.RequestLoginCodeForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "signup": "allauth.account.forms.SignupForm",
    "user_token": "allauth.account.forms.UserTokenForm",
}

ACCOUNT_LOGIN_BY_CODE_ENABLED = False

ACCOUNT_LOGIN_BY_CODE_MAX_ATTEMPTS = 3

ACCOUNT_LOGIN_BY_CODE_REQUIRED = False

ACCOUNT_LOGIN_BY_CODE_TIMEOUT = 180

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

ACCOUNT_LOGIN_ON_PASSWORD_RESET = False

ACCOUNT_LOGIN_TIMEOUT = 900

ACCOUNT_LOGOUT_ON_GET = False

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = False

ACCOUNT_LOGOUT_REDIRECT_URL = "/"

ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = False

ACCOUNT_PASSWORD_RESET_TOKEN_GENERATOR = (
    "allauth.account.forms.EmailAwarePasswordResetTokenGenerator"
)

ACCOUNT_PRESERVE_USERNAME_CASING = True

ACCOUNT_PREVENT_ENUMERATION = True

ACCOUNT_RATE_LIMITS = {
    "change_password": "5/m/user",
    "manage_email": "10/m/user",
    "reset_password": "20/m/ip,5/m/key",
    "reauthenticate": "10/m/user",
    "reset_password_from_key": "20/m/ip",
    "signup": "20/m/ip",
    "login": "30/m/ip",
    "login_failed": "10/m/ip,5/5m/key",
    "confirm_email": "1/3m/key",
}

ACCOUNT_REAUTHENTICATION_TIMEOUT = 300

ACCOUNT_REAUTHENTICATION_REQUIRED = True

ACCOUNT_SESSION_REMEMBER = None

ACCOUNT_SIGNUP_REDIRECT_URL = "/"

ACCOUNT_TEMPLATE_EXTENSION = "html"

# ACCOUNT_USERNAME_BLACKLIST = []

# ACCOUNT_UNIQUE_EMAIL = True

# ACCOUNT_USER_DISPLAY = None  # user.username

ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"

ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"

ACCOUNT_USERNAME_MIN_LENGTH = 4

ACCOUNT_USERNAME_REQUIRED = False

# ACCOUNT_USERNAME_VALIDATORS = None

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]
