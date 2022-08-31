import dj_database_url

from .base import *



ALLOWED_HOSTS = ['*.herokuapp.com', 'blog-inf.herokuapp.com']
DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)