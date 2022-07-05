from rest_framework import serializers
from .models import *
from upload.models import Image
from upload.serializers import ImageSerializer


class MyNewsSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    image_id = serializers.PrimaryKeyRelatedField(
        queryset=Image.objects.all(), source='image'
    )

    class Meta:
        model = MyNews
        fields = [
            'id',
            'title',
            'excerpt',
            'content',
            'image',
            'image_id',
            'created_datetime',
            'update_datetime',
            'status'
        ]
