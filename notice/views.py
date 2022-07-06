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

    def post(self, request, *args, **kwargs):

        print("Hi")
        print(request)
        print(request.data)
        print(request.data['body'])

        return response.Response(1)
