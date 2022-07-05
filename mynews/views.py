from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import permissions, viewsets, response
from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'per'
    page_query_param = 'p'


# Create your views here.


class MyNewsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MyNewsSerializer
    queryset = MyNews.objects.filter(status='publish')
    pagination_class = StandardResultsSetPagination
