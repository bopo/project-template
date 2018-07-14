import importlib
from importlib import import_module

from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import six
from six import string_types


def import_callable(path_or_callable):
    if hasattr(path_or_callable, '__call__'):
        return path_or_callable
    else:
        assert isinstance(path_or_callable, string_types)
        package, attr = path_or_callable.rsplit('.', 1)
        return getattr(import_module(package), attr)


def user_field(user, field, *args):
    """
    Gets or sets (optional) user model fields. No-op if fields do not exist.
    """
    if field and hasattr(user, field):
        if args:
            # Setter
            v = args[0]
            if v:
                User = get_user_model()
                v = v[0:User._meta.get_field(field).max_length]
            setattr(user, field, v)
        else:
            # Getter
            return getattr(user, field)


def user_username(user, *args):
    return user_field(user, settings.USER_MODEL_USERNAME_FIELD, *args)


def user_email(user, *args):
    return user_field(user, settings.USER_MODEL_EMAIL_FIELD, *args)


def import_attribute(path):
    assert isinstance(path, six.string_types)

    pkg, attr = path.rsplit('.', 1)
    ret = getattr(importlib.import_module(pkg), attr)

    return ret
