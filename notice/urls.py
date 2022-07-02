from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'broker', BrokerViewSet)
router.register(r'signal', SignalAlertViewSet)

urlpatterns = router.urls
