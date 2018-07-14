# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib import auth
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .settings import (
    LoginSerializer,
    PasswordChangeSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    TokenSerializer
)


class SocialView(GenericAPIView):
    '''
    如果用户登陆状态则为绑定
    如果用户为登陆状态则为登陆
    如果用户之前没有注册，则为注册并绑定
    用户名则为随机生成
    用户以手机号为主要登陆方式
    '''
    token_model = Token
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    response_serializer = TokenSerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def get_response(self):
        return Response(self.response_serializer(self.token).data, status=status.HTTP_200_OK)

    def get_error_response(self):
        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)

        if not self.serializer.is_valid():
            return self.get_error_response()

        # self.login()
        return self.get_response()


class LoginView(GenericAPIView):
    """
    登录接口

    POST 提交参数: mobile, password,
    返回的 key 是 toke n的值.

    请使用下面的正则表达式验证手机号码正确性，在提交服务器前客户端提交一次
    手机号码验证正则表达式：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
    """
    token_model = Token
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    response_serializer = TokenSerializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token, created = self.token_model.objects.get_or_create(user=self.user)

        if getattr(settings, 'REST_SESSION_LOGIN', True):
            auth.login(self.request, self.user)

    def get_response(self):
        return Response(self.response_serializer(self.token).data, status=status.HTTP_200_OK)

    def get_error_response(self):
        return Response(self.serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        self.serializer = self.get_serializer(data=self.request.data)

        if not self.serializer.is_valid(raise_exception=True):
            return self.get_error_response()

        self.login()
        return self.get_response()


class LogoutView(APIView):
    """
    注销接口

    Calls logout method and delete the Token object
    assigned to the current User object.

    Accepts/Returns nothing.
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        try:
            request.user.auth_token.delete()
        except:
            pass

        auth.logout(request)
        return Response({"detail": "注销成功."}, status=status.HTTP_200_OK)


"""
Calls Django Auth PasswordResetForm save method.

Accepts the following POST parameters: mobile
Returns the success/fail message.
"""


class PasswordResetView(GenericAPIView):
    '''
    修改密码

    请使用下面的正则表达式验证手机号码正确性，在提交服务器前客户端提交一次
    手机号码验证正则表达式：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
    '''
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'detail': u'验证码已经成功发送'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        # 发送短信代码
        pass
        # serializer.save()


class PasswordResetConfirmView(GenericAPIView):
    """
    重置密码确认

    Password reset e-mail link is confirmed, therefore this resets the user's password.

    Accepts the following POST parameters: new_password1, new_password2
    Accepts the following Django URL arguments: token, uid
    Returns the success/fail message.
    """
    serializer_class = PasswordResetConfirmSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'detail': u'密码重置成功'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()


class PasswordChangeView(GenericAPIView):
    """
    重置密码接口
    
    Calls Django Auth SetPasswordForm save method.

    Accepts the following POST parameters: new_password1, new_password2
    Returns the success/fail message.
    """
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'detail': u'密码修改成功'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save()
