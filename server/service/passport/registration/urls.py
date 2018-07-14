# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = (
    path('', views.RegisterView.as_view(), name='rest_register'),
    path('verify_mobile/', views.VerifyMobileView.as_view(), name='rest_verify_mobile'),
)
