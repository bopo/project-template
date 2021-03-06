# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..serializers import RegisterSerializer, VerifySerializer
from ..settings import TokenSerializer
from .forms import SignupForm


class RegisterView(GenericAPIView):
    '''
    注册接口

    注意：

    手机注册前，先请求 `/auth/signup/verify_mobile/` 接口, 获取 verify code.

    请使用下面的正则表达式验证手机号码正确性，在提交服务器前客户端提交一次
    手机号码验证正则表达式：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
    '''
    token_model = Token
    form_class = SignupForm
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    response_serializer = TokenSerializer
    queryset = get_user_model().objects.all()
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def form_valid(self, form):
        self.user = form.save(self.request)
        self.token, created = self.token_model.objects.get_or_create(user=self.user)

        return self.token

    def post(self, request, *args, **kwargs):
        self.form = self.form_class(request.data)

        if self.form.is_valid():
            self.form_valid(self.form)
            return self.get_response()

        return self.get_response_with_errors()

    def get_response(self):
        serializer = self.response_serializer(instance=self.token)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_response_with_errors(self):
        return Response(self.form.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyMobileView(GenericAPIView):
    '''
    发送手机验证码
    
    注意：

    请使用下面的正则表达式验证手机号码正确性，在提交服务器前客户端提交一次
    手机号码验证正则表达式：^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$
    '''
    permission_classes = (AllowAny,)
    serializer_class = VerifySerializer
    allowed_methods = ('POST', 'OPTIONS', 'HEAD')

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'detail': u'验证码已经成功发送'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        pass
