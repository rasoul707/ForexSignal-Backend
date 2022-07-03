from rest_framework import serializers
from .models import License
from appsetting.models import AppSetting


class LicenseSerializerAccount(serializers.ModelSerializer):

    is_trial = serializers.SerializerMethodField('is_trial_license')

    def is_trial_license(self, foo):
        bb = AppSetting.objects.get(pk=1)
        print("M", bb)
        print("B", bb.trial_license)

        return foo.id == AppSetting.objects.get(pk=1).trial_license

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
