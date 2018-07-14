# import short_url
import short_url
from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Notification, Profile
from .serializers import AvatarSerializer, NotificationSerializer, ProfileSerializer
from .utils import get_user_profile


class ProfileViewSet(RetrieveUpdateAPIView):
    '''
    用户信息
    '''
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #
    #     data = serializer.data
    #     data['qrcode'] = reverse('qr', args=[short_url.encode_url(instance.pk)], request=request)
    #
    #     return Response(data)

    def get_object(self):
        return get_user_profile(self.request.user)


class AvatarViewSet(RetrieveUpdateAPIView):
    '''
    头像上传接口.

    '''
    serializer_class = AvatarSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_user_profile(self.request.user)


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Notification.objects.filter(owner=self.request.user)

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()

        return queryset
