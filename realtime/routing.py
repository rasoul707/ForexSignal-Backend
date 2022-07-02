# chat/routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/signalsAlert', consumers.SignalsAlertWS.as_asgi()),
    re_path(r'ws/articles', consumers.ArticlesWS.as_asgi()),
]
