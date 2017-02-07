'''
# Define your own DB connection.
# if none is defined, a default SQLite file will be used at /db.sqlite3
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'NAME':     'db name',
        'USER':     'db user',
        'PASSWORD': 'db password',
        'HOST':     'localhost',
    }
}
'''

MY_APPS = ['my_customizations_app',]