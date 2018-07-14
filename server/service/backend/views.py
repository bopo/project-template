# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.permissions import IsAuthenticated

from .models.common import Feedback, Version, BankAccount
from .serializers import FeedbackSerializer, VersionsSerializer, BankAccountSerializer


class BankAccountViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    手机应用版本更新接口
    '''
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer

class VersionsViewSet(viewsets.ReadOnlyModelViewSet):
    '''
    手机应用版本更新接口
    '''
    queryset = Version.objects.order_by('-id')
    serializer_class = VersionsSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_fields = ('platform', 'channel')


class FeedbackViewSet(viewsets.ModelViewSet):
    '''
    意见反馈接口
    '''
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    # permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

