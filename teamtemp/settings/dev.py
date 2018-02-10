import dj_database_url

from teamtemp.settings.base import *

DEBUG = os.environ.get('DJANGO_DEBUG', True)
SECRET_KEY = os.environ.get(
    'TEAMTEMP_SECRET_KEY',
    'rp47vufz8lrr1cxki7lmc9w221ajgauk5ctv6xj')


if ON_HEROKU:
    DATABASE_URL = 'postgresql:///postgresql'
else:
    DATABASE_URL = 'sqlite://' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': os.path.join(PROJECT_DIR, 'teamtemp.postgresql'),
#    }
# }

# Update database configuration with $DATABASE_URL.
# DATABASES['default'].update(
#    dj_database_url.config(conn_max_age=600)
# )
