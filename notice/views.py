from django.shortcuts import render

from .models import *
from .serializers import *
from rest_framework import permissions, viewsets, response, views
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per'
    page_query_param = 'p'


class SignalAlertViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SignalAlertSerializer
    pagination_class = None
    filterset_fields = ['broker']
    queryset = SignalAlert.objects.all()
    # permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            SignalAlert.objects.filter(is_active=True)
        )
        serializer = self.get_serializer(queryset, many=True)
        return response.Response(serializer.data)


class BrokerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BrokerSerializer
    queryset = Broker.objects.all()


class NewSignal(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        broker = self.request.query_params.get('br')
        symbol = self.request.query_params.get('sy')
        time_frame = self.request.query_params.get('tf')
        direction = self.request.query_params.get('dir')

        br = Broker.objects.get_or_create(name=broker)

        signal = SignalAlert(
            broker=br,
            title=symbol,
            description=direction + "," + time_frame
        )

        signal.save()

        return response.Response(1)
