from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path("ws/payment", consumers.NotificationConsumer.as_asgi()),
]