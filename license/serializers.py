from rest_framework import serializers
from .models import License


class LicenseSerializerAccount(serializers.ModelSerializer):

    class Meta:
        model = License
        fields = [
            'id',
            'title',
            'unlimited'
        ]


class LicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = License
        fields = [
            'id',
            'title',
            'price',
            'description',
            'is_active',
            'unlimited',
            'duration'
        ]
