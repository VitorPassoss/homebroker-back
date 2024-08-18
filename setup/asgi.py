import os

import django
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "setup.settings")

django.setup()

from apps.staffs.routing import (
    websocket_urlpatterns as staffs_ws_url,
)

all_ws_urls = staffs_ws_url

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": OriginValidator(
            AuthMiddlewareStack(
                URLRouter(
                    all_ws_urls,
                )
            ),
            ["*"],
        ),
    }
)