from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import permissions, viewsets, response

# Create your views here.


class MyNewsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MyNewsSerializer
    queryset = MyNews.objects.all()
