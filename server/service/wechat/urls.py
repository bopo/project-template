# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = (
    path('', views.gateway),
    path('weapp', views.weapp),
    path('payment', views.payment),
    path('userinfo', views.userinfo),
)
