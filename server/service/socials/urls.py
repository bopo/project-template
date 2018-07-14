"""URLs module"""
from django.conf import settings
from django.urls import path

from . import views
from .contrib.core.utils import setting_name

extra = getattr(settings, setting_name('TRAILING_SLASH'), True) and '/' or ''

app_name = 'social'

urlpatterns = [
    # authentication / association
    path('login/<str:backend>'.format(extra), views.auth, name='begin'),
    path('complete/<str:backend>'.format(extra), views.complete, name='complete'),

    # disconnection
    path('disconnect/<str:backend>'.format(extra), views.disconnect, name='disconnect'),
    path('disconnect/<str:backend>/<str:association_id>'.format(extra), views.disconnect, name='disconnect_individual'),
]
