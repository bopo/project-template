# coding=utf-8
from functools import wraps

from django.conf import settings
from django.http import Http404
from django.urls import reverse

from .contrib.core.backends.utils import get_backend
from .contrib.core.utils import get_strategy, module_member, setting_name
from .exceptions import MissingBackend

BACKENDS = settings.AUTHENTICATION_BACKENDS
STRATEGY = getattr(settings, setting_name('STRATEGY'), 'service.socials.strategy.DjangoStrategy')
Strategy = module_member(STRATEGY)

STORAGE = getattr(settings, setting_name('STORAGE'), 'service.socials.models.DjangoStorage')
Storage = module_member(STORAGE)


def load_strategy(request=None):
    return get_strategy(STRATEGY, STORAGE, request)


def load_backend(strategy, name, redirect_uri):
    Backend = get_backend(BACKENDS, name)
    return Backend(strategy, redirect_uri)


def psa(redirect_uri=None, load_strategy=load_strategy):
    def decorator(func):
        @wraps(func)
        def wrapper(request, backend, *args, **kwargs):
            uri = redirect_uri
            
            if uri and not uri.startswith('/'):
                uri = reverse(redirect_uri, args=(backend,))

            request.social_strategy = load_strategy(request)
            # backward compatibility in attribute name, only if not already
            # defined
            if not hasattr(request, 'strategy'):
                request.strategy = request.social_strategy

            try:
                request.backend = load_backend(request.social_strategy,
                                               backend, uri)
            except MissingBackend:
                raise Http404('Backend not found')
            
            return func(request, backend, *args, **kwargs)

        return wrapper

    return decorator