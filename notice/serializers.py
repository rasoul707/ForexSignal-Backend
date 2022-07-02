from rest_framework import serializers
from .models import *
from upload.models import Image
from upload.serializers import ImageSerializer


class SignalAlertSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    image_id = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), source='image',
    )

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
            'is_active',
            'image',
            'image_id',
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
