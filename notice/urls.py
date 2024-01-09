from django.urls import path

from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'broker', BrokerViewSet)
router.register(r'signal', SignalAlertViewSet)
# router.register(r'new', NewSignal.as_view())

urlpatterns = router.urls + [path('new', NewSignal.as_view()), path('result', SignalResult.as_view())]
