import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

DEBUG = os.getenv('DEBUG')
ALLOWED_HOSTS = ['*']
# if DEBUG == 'False':
#     from dotenv import dotenv_values
#     config = dotenv_values("env/.local")
#     ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yj^vfxi_!f7!jo93#i^c(@+ilqoz6lnm*&84rpt!3r(tod390h'

# SECURITY WARNING: don't run with debug turned on in production!


# Application definition
INSTALLED_APPS = [
    'drf_yasg',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # local apps
    'users',
    # third
    'rest_framework',
    'application',
    'modeltranslation',
    'rest_framework_simplejwt.token_blacklist',
    "corsheaders",

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]
AUTH_USER_MODEL = "users.CustomUser"

ROOT_URLCONF = 'application.urls'

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

WSGI_APPLICATION = 'application.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

}
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("POSTGRES_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("POSTGRES_DB", os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": os.environ.get("POSTGRES_USER", "user"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "password"),
        "HOST": os.environ.get("POSTGRES_HOST", "localhost"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Tashkent'
# LOCALE_PATHS = (os.path.join(BASE_DIR, "locale"),)

USE_I18N = True

USE_TZ = True
gettext = lambda s: s
LANGUAGES = (
    ('uz', gettext('Uzbek')),
    ('en', gettext('English')),
    ('ru', gettext('Russian')),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_TRANSLATION_REGISTRY = 'application.translation'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
MEDIA_URL = '/media/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# SimpleJWT Settings
SIMPLE_JWT = {
    # Token Lifetimes
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),  # Short-lived access tokens
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Long-lived refresh tokens

    # Token Rotation and Blacklisting
    'ROTATE_REFRESH_TOKENS': True,  # Generate a new refresh token on each use
    'BLACKLIST_AFTER_ROTATION': True,  # Blacklist the old refresh token after rotation

    # Token Settings
    'ALGORITHM': 'HS256',  # Algorithm used to sign tokens
    'SIGNING_KEY': SECRET_KEY,  # Default signing key (use a secure key in production)
    'VERIFYING_KEY': None,  # Used for asymmetric algorithms (e.g., RS256)
    'AUDIENCE': None,
    'ISSUER': None,

    # Token Types
    'AUTH_HEADER_TYPES': ('Bearer',),  # Authorization header prefix (e.g., 'Bearer <token>')
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),

    # Sliders for Time Skew and Expiry
    'LEEWAY': 0,  # Time leeway to account for clock differences

    # Blacklist Settings (if using the token_blacklist app)
    'TOKEN_TYPE_CLAIM': 'token_type',  # Claim name for token type (access/refresh)
    'JTI_CLAIM': 'jti',  # Unique identifier claim for blacklist support

    # Token Customization
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),  # For sliding tokens (optional)
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# CSRF settings
CSRF_TRUSTED_ORIGINS = os.environ.get('CSRF_ALLOWED_ORIGINS', 'http://0.0.0.0:8020').split(',')

# CORS settings
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', 'http://0.0.0.0:8020').split(',')
CORS_TRUSTED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', 'http://0.0.0.0:8020').split(',')


CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'authorizations',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
CORS_EXPOSE_HEADERS = ['Content-Type', 'X-CSRFToken', 'Access-Control-Allow-Origin']

CORS_ALLOW_CREDENTIALS = True