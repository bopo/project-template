# -*- coding: utf-8 -*-
from dashing.utils import router
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

# from service.dashboard.site import DashboardSite

# admin.site = DashboardSite()
# admin.sites.site = admin.site
# admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('service.openapi.urls')),
    path('', include('service.frontend.urls')),
    path('api/', include('service.backend.urls')),

    path('dashboard/', include(router.urls)),
    path('payments/', include('payments.urls')),
    path('accounts/', include('allauth.urls')),
    path('social/', include('service.socials.urls')),
    # path('explore/', include('haystack.urls')),

    path('robots.txt', RedirectView.as_view(url='/static/robots.txt', permanent=True)),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar

#     # This allows the error pages to be debugged during development, just visit
#     # these url in browser to see how these error pages look like.
#     urlpatterns += [
#         # re_path(r'^400/$', default_views.bad_request, kwargs={'exception': Exception("Bad Request!")}),
#         # re_path(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception("Permission Denied")}),
#         # re_path(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception("Page not Found")}),
#         # re_path(r'^500/$', default_views.server_error),

#     	path('docs/', get_swagger_view(title='API docs')),
#     	path('silk/', include('silk.urls', namespace='silk')),
#     ] 

#     # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
#     urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),] + urlpatterns
