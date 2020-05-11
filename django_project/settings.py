"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ngbgtwu*my@ws%z7y4mszc0yq)yp+zi-9jrxc3chs7&j9-+^(v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '192.168.1.5']

# Application definition

INSTALLED_APPS = [

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my Apps
    'debug_toolbar',
    'import_export',
    'crispy_forms',
    'customers',
    'machines',
    'services',
    'login',
    'Calendar',
    'service_data',
    'companies',
    'spareparts',
    'receiver_emails',
    'sender_emails',
    'Copiers_Log',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'Service_book.db'),
    },
    'SparePartsDb': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db'),

    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'el-GR'

TIME_ZONE = 'Europe/Athens'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")
MEDIA_ROOT = os.path.join(BASE_DIR, "Media/Service_images/")
MEDIA_URL = "/Media/Service_images/"
# STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    "localhost",
    "192.168.1.5",
    # ...
]

# https://docs.djangoproject.com/en/3.0/ref/settings/
DATE_FORMAT = (
    '%d.%m.%Y', '%d.%m.%Y', '%d.%m.%y',  # '25.10.2006', '25.10.2006', '25.10.06'
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y',  # '25-10-2006', '25/10/2006', '25/10/06'
    '%d %b %Y',  # '25 Oct 2006',
    '%d %B %Y',  # '25 October 2006',
)

DATE_INPUT_FORMATS = (
    '%d.%m.%Y', '%d.%m.%Y', '%d.%m.%y',  # '25.10.2006', '25.10.2006', '25.10.06'
    '%d-%m-%Y', '%d/%m/%Y', '%d/%m/%y',  # '25-10-2006', '25/10/2006', '25/10/06'
    '%d %b %Y',  # '25 Oct 2006',
    '%d %B %Y',  # '25 October 2006',
)

# https://docs.djangoproject.com/en/3.0/topics/auth/default/#the-login-required-decorator
LOGIN_URL = 'login:login'

# DIsable  DEBUG_TOOLBAR
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda r: False,  # disables it
    # '...
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-SESSION_ENGINE
CSRF_COOKIE_DOMAIN = '127.0.0.1'

#  If this is set to True, client-side JavaScript will not be able to access the session cookie.
SESSION_COOKIE_HTTPONLY = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 600  # 10 Min
SESSION_SAVE_EVERY_REQUEST = True

# If this is set to True, the cookie will be marked as “secure”,
#  which means browsers may ensure that the cookie is only sent under an HTTPS connecion
SESSION_COOKIE_SECURE = False

CSRF_COOKIE_HTTPONLY = True
CSRF_USE_SESSIONS = True
SECURE_SSL_REDIRECT = False
SESSION_ENGINE = "django.contrib.sessions.backends.db"
LOGIN_REDIRECT_URL = '/Calendar'
