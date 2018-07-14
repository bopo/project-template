# -*- coding: utf-8 -*-
from django.urls import include, path

from . import views
from .registration import urls as registration_urls

urlpatterns = (
    path('password/reset/confirm/', views.PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('password/change/', views.PasswordChangeView.as_view(), name='rest_password_change'),
    path('password/reset/', views.PasswordResetView.as_view(), name='rest_password_reset'),

    path('logout/', views.LogoutView.as_view(), name='rest_logout'),
    path('signin/', views.LoginView.as_view(), name='rest_signin'),
    path('signup/', include(registration_urls)),

    # path('social/', include('service.socials.urls', namespace='rest_social'))
)
