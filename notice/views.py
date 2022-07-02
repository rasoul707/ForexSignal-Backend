from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import permissions, viewsets, response

# Create your views here.


class SignalAlertViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SignalAlertSerializer
    pagination_class = None
    filterset_fields = ['broker']
    queryset = SignalAlert.objects.all()
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            SignalAlert.objects.filter(is_active=True)
        )
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class BrokerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()
