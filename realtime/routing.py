from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    # re_path(r'ws/news', consumers.NewsWS.as_asgi()),
    re_path(r'ws/signal(?P<broker_id>\w+)/$',
            consumers.SignalsAlertWS.as_asgi()
            ),
]
