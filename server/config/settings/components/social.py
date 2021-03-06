INSTALLED_APPS += ('service.socials',)

AUTHENTICATION_BACKENDS = (
    'service.socials.contrib.core.backends.qq.QQOAuth2',  # QQ的功能
    'service.socials.contrib.core.backends.weibo.WeiboOAuth2',  # 微博的功能

    'service.socials.contrib.core.backends.weixin.WeixinOAuth2',  # 这个是导入微信的功能
    'service.socials.contrib.core.backends.weixin.WeixinOAuth2APP',  # 这个是导入微信的功能

    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'service.socials.contrib.core.backends.qq.QQOAuth2',  # QQ的功能
    'service.socials.contrib.core.backends.weibo.WeiboOAuth2',  # 微博的功能

    'service.socials.contrib.core.backends.weixin.WeixinOAuth2',  # 这个是导入微信的功能
    'service.socials.contrib.core.backends.weixin.WeixinOAuth2APP',  # 这个是导入微信的功能
)

SOCIAL_AUTH_PIPELINE = (
    'service.socials.contrib.core.pipeline.social_auth.social_details',
    'service.socials.contrib.core.pipeline.social_auth.social_uid',
    'service.socials.contrib.core.pipeline.social_auth.social_user',
    'service.socials.contrib.core.pipeline.user.get_username',
    'service.socials.contrib.core.pipeline.user.create_user',
    'service.socials.contrib.core.pipeline.social_auth.associate_user',
    'service.socials.contrib.core.pipeline.social_auth.load_extra_data',
    'service.socials.contrib.core.pipeline.user.user_details',
    'service.socials.contrib.core.pipeline.social_auth.associate_by_email',
)

SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']
