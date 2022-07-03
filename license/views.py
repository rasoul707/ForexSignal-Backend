
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.


class LicenseViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LicenseSerializer
    queryset = License.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(
            License.objects.filter(is_private=False)
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
