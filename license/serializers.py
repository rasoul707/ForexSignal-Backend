from rest_framework import serializers
from .models import License


class LicenseSerializerAccount(serializers.ModelSerializer):

    is_trial = serializers.SerializerMethodField('is_trial_license')

    def is_trial_license(self, foo):
        return foo.id == 1

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
