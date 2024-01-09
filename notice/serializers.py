from rest_framework import serializers
from .models import *
from upload.models import Image
from upload.serializers import ImageSerializer


class SignalAlertSerializer(serializers.ModelSerializer):

    broker_id = serializers.PrimaryKeyRelatedField(
        queryset=Broker.objects.all(), source='broker'
    )

    class Meta:
        model = SignalAlert
        fields = [
            'id',
            'title',
            'description',
            'broker',
            'broker_id',
            'percent',
            'winrate',
            'is_active',
            'detail',
            'created_datetime'
        ]
        depth = 1


class BrokerSerializer(serializers.ModelSerializer):
    logo = ImageSerializer()
    logo_id = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), source='logo'
    )

    class Meta:
        model = Broker
        fields = [
            'id',
            'name',
            'logo',
            'logo_id',
        ]
