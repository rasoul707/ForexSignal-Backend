from rest_framework import serializers
from .models import License


class LicenseSerializerAccount(serializers.ModelSerializer):

    is_trial = True

    class Meta:
        model = License
        fields = [
            'title',
            'unlimited',
            'is_trial'
        ]


class LicenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = License
        fields = [
            'id',
            'title',
            'price',
            'description',
            'unlimited',
            'duration'
        ]
