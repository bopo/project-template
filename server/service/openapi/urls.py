from django.urls import include, path

urlpatterns = (
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)
