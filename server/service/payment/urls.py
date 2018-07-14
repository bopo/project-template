from django.urls import include, path

urlpatterns = (
    path('wechat/', include('wechat.urls', namespace='wechat_provider')),
    path('alipay/', include('alipay.urls', namespace='alipay_provider')),
)
