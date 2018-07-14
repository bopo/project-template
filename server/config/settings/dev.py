# -*- coding: utf-8 -*-
from split_settings.tools import include, optional

include(
    'components/base.py',
    'components/apps.py',
    'components/rest.py',
    'components/auth.py',
    # 'components/logs.py',
    'components/suit.py',
    'components/pays.py',

    'components/static.py',
    'components/social.py',
    'components/celery.py',
    'components/search.py',

    'components/const.py',
    # 'components/const.py',
    # 'components/cache.py',
    # 'components/email.py',
    # 'components/thumb.py',
    # 'components/store.py',

    optional('components/debug.py'),
)

DEBUG = env('DJANGO_DEBUG', default=True)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(ROOT_DIR.path('db.sqlite3')),
    }
}
