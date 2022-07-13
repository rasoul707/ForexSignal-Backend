
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.


class AppSettingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AppSettingSerializer
    queryset = AppSetting.objects.all()
