from rest_framework import serializers

from .models import Notification, Profile


class ProfileSerializer(serializers.ModelSerializer):
    ''' 用户信息 '''

    class Meta:
        model = Profile
        read_only_fields = ("level", 'credit', 'avatar')
        exclude = ('owner',)


class AvatarSerializer(serializers.ModelSerializer):
    ''' 头像序列 '''

    class Meta:
        model = Profile
        fields = ('avatar',)


class NotificationSerializer(serializers.ModelSerializer):
    ''' 消息序列 '''

    class Meta:
        model = Notification
        fields = ('subject', 'content', 'created')
