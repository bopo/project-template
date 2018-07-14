# -*- coding: utf-8 -*-

INSTALLED_APPS += (
    'service.frontend',
    'service.customer',
    'service.discover',

    'service.openapi',
    'service.backend',
    # 'service.payment',

    'service.passport',
    'service.passport.registration',
    'service.wechat',

    'service.dashboard',
    'django_extensions',
    
    # 'import_export',
    'reversion',
    # 'channels',
    # 'haystack',
    'imagekit',
    # 'channels',
    'filters',

    'dashing',
    'djmoney',
)

ASGI_APPLICATION = "config.routing.application"
