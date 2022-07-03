from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
# Create your views here.


class LicenseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()
