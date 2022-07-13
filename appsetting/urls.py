from rest_framework import routers
from .views import *


router = routers.DefaultRouter()

router.register(r'setting', AppSettingViewSet)


urlpatterns = router.urls
