from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'notification', views.NotificationViewSet, 'me-notices')

urlpatterns = (
    path('', include(router.urls)),
    path('profile/', views.ProfileViewSet.as_view(), name='me-profile'),
    path('profile/avatar/', views.AvatarViewSet.as_view(), name='profile-avatar'),
)
