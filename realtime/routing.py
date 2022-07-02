from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/fx/signals', consumers.SignalsAlertWS.as_asgi()),
    re_path(r'ws/fx/articles', consumers.ArticlesWS.as_asgi()),
]
