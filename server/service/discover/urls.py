# -*- coding: utf-8 -*-

from django.urls import include, path
from rest_framework import routers

from .views import LocationSearchView

router = routers.DefaultRouter()
router.register("location", LocationSearchView, base_name="location-search")


urlpatterns = (
    path("", include(router.urls)),
)
