import dj_database_url

from teamtemp.settings.base import *

DEBUG = os.environ.get('DJANGO_DEBUG', True)
SECRET_KEY = os.environ.get(
    'TEAMTEMP_SECRET_KEY',
    'rp47vufz8lrr1cxki7lmc9w221ajgauk5ctv6xj')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.path.join(PROJECT_DIR, 'teamtemp.postgresql'),
    }
}

# Update database configuration with $DATABASE_URL.
DATABASES['default'].update(
    dj_database_url.config(conn_max_age=600)
)
