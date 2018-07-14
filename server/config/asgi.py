# -*- coding: utf-8 -*-
import os

import django
from channels.routing import get_default_application


def get_asgi_application():
    django.setup(set_prefix=False)
    return get_default_application()


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

application = get_asgi_application()
