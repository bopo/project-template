from rest_framework import serializers

from ..models.common import Version, Feedback, BankAccount


class VersionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
