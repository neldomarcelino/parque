"""
Django settings for parque project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'mfbwt39&j4@m4u7qko@sda$74rn-$81nj#24#s_^hdo^p0i-_v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'inaturalist.apps.InaturalistConfig',
    'speciesImage.apps.SpeciesimageConfig',
    'location.apps.LocationConfig',
    'district.apps.DistrictConfig',
    'province.apps.ProvinceConfig',
    'region.apps.RegionConfig',
    'geography.apps.GeometryConfig',
    'person.apps.PersonConfig',
    'identifier.apps.IdentifierConfig',
    'actor.apps.ActorConfig',
    'species.apps.SpeciesConfig',
    'genero.apps.GeneroConfig',
    'ordem.apps.OrdemConfig',
    'familia.apps.FamiliaConfig',
    'classe.apps.ClasseConfig',
    'home.apps.HomeConfig',
    'filo.apps.FiloConfig',
    'reino.apps.ReinoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',

    'colorfield',
    'leaflet',
    'djgeojson',

    'django_plotly_dash.apps.DjangoPlotlyDashConfig',
    'channels',
    'bootstrap4',
    'dpd_static_support',
    'rest_framework',
    # 'admin_black.apps.AdminBlackConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',


    'django_plotly_dash.middleware.BaseMiddleware',
    'django_plotly_dash.middleware.ExternalRedirectionMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

]



ROOT_URLCONF = 'parque.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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
X_FRAME_OPTIONS = 'SAMEORIGIN'
WSGI_APPLICATION = 'parque.wsgi.application'
ASGI_APPLICATION = 'parque.routing.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',
        'ENGINE': 'django.contrib.gis.db.backends.mysql',

        # 'NAME': 'parkarea',
        # 'USER': 'digio',
        # 'PASSWORD': '#D!g(o+*12.=?@m',

        'NAME': 'htbj73rpm8uhigv0',
        'USER': 'mu4jjnj8rxtdl5km',
        'PASSWORD': 'n9wfg1g8ul9cp7uw',
        'HOST': 'eyvqcfxf5reja3nv.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',

    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# Plotly dash settings

PLOTLY_DASH = {
    "ws_route" : "ws/channel",

    "insert_demo_migrations" : True,  # Insert model instances used by the demo

    "http_poke_enabled" : True, # Flag controlling availability of direct-to-messaging http endpoint

    "view_decorator" : None, # Specify a function to be used to wrap each of the dpd view functions

    "cache_arguments" : True, # True for cache, False for session-based argument propagation

    #"serve_locally" : True, # True to serve assets locally, False to use their unadulterated urls (eg a CDN)

    "stateless_loader" : "demo.scaffold.stateless_app_loader",
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = 'staticfiles'



LEAFLET_CONFIG = {
    # conf here
    'DEFAULT_CENTER': (-13, 39.0),
    'DEFAULT_ZOOM': 16,
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
    'DEFAULT_PRECISION': 12,
    'SCALE': 'both',
    'FORCE_IMAGE_PATH': True,
    # 'MINIMAP': True,
    # 'SPATIAL_EXTENT': (250, 300,-50, -40),
}
LEAFLET_SETTINGS = {

}
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [('127.0.0.1', 6379),],
        },
    },
}
STATICFILES_FINDERS = [

    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

    'django_plotly_dash.finders.DashAssetFinder',
    'django_plotly_dash.finders.DashComponentFinder',
    'django_plotly_dash.finders.DashAppDirectoryFinder',
]
PLOTLY_COMPONENTS = [
    'dash_core_components',
    'dash_html_components',
    'dash_bootstrap_components',
    'dash_renderer',
    'dpd_components',
    'dpd_static_support',
]
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}