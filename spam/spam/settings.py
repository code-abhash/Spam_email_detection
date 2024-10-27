
from pathlib import Path


# Define BASE_DIR as a Path object
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
# settings.py





SECRET_KEY = 'ath!5052_d9^8)j9o@1h+o^w%r3zaqyr8q#g8l(5u&8)!q^x1u'
DEBUG =True



# Allowed hosts (update with your Vercel deployment URL)
ALLOWED_HOSTS = ['*']  # Replace with your actual domain

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'spam_app',  # Ensure your app is listed here
    'whitenoise.runserver_nostatic',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spam.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'spam_app' / 'templates'],  # Ensure this points to your templates
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

WSGI_APPLICATION = 'spam.wsgi.application'

# No database required for this application
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Use if needed, otherwise comment out
        'NAME': BASE_DIR / 'db.sqlite3',  # Comment out if not using
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Vercel specific static file settings
STATICFILES_DIRS = [BASE_DIR / 'spam_app' / 'static']  # Where to find static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where to collect static files

# Ensure Whitenoise is included in your middleware
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')

# Default auto field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
