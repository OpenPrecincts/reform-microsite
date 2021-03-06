import os
import dj_database_url

PREFIX = "reforms2019/"


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if os.environ.get("DEBUG", "true").lower() == "false":
    # production settings
    DEBUG = False
    ALLOWED_HOSTS = ["*"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    # ADMINS list should be 'Name Email, Name Email, Name Email...'
    ADMINS = [a.rsplit(" ", 1) for a in os.environ.get("ADMINS", "").split(",")]
    EMAIL_HOST = os.environ["EMAIL_HOST"]
    EMAIL_HOST_USER = os.environ["EMAIL_HOST_USER"]
    EMAIL_HOST_PASSWORD = os.environ["EMAIL_HOST_PASSWORD"]
    EMAIL_PORT = "587"
    EMAIL_USE_TLS = True
    REGISTRATION_DEFAULT_FROM_EMAIL = (
        DEFAULT_FROM_EMAIL
    ) = SERVER_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "bounce@openprecincts.org")
else:
    # dev settings
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "debug-secret-key")
    ALLOWED_HOSTS = ["*"]
    INTERNAL_IPS = ["127.0.0.1"]
    DOMAIN = "http://localhost:8000"
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://localhost/reforms")
DATABASES = {"default": dj_database_url.parse(DATABASE_URL)}
CONN_MAX_AGE = 60


# non-dynamic configuration

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "reforms",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    # "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

AUTHENTICATION_BACKENDS = ["django.contrib.auth.backends.ModelBackend"]

ROOT_URLCONF = "web.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "web.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = "/" + PREFIX + "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# third party apps
WEBPACK_LOADER = {
    "DEFAULT": {
        "CACHE": not DEBUG,
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats.json"),
        "POLL_INTERVAL": 0.1,
        "TIMEOUT": None,
        "IGNORE": [r".+\.hot-update.js", r".+\.map"],
    }
}
