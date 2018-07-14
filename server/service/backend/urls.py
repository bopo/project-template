# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from .views import FeedbackViewSet, VersionsViewSet, BankAccountViewSet

router = DefaultRouter()
router.register('feedback', FeedbackViewSet, base_name='feedback')
router.register('versions', VersionsViewSet, base_name='versions')
router.register('accounts', BankAccountViewSet, base_name='accounts')

urlpatterns = (
    path('', include(router.urls)),
    path('me/', include('service.customer.urls')),
    path('wx/', include('service.wechat.urls')),
    path('so/', include('service.discover.urls')),
    # path('im/', include('service.message.urls')),

    # path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('token/auth/', obtain_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('token/refresh/', refresh_jwt_token),

    path('auth/', include('service.passport.urls')),
    path('rest/', include('rest_framework.urls', namespace='rest_framework')),
)
