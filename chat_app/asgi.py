import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')
import django
django.setup()

from channels.routing import URLRouter,ProtocolTypeRouter
from app.routing import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator




application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AllowedHostsOriginValidator(
    AuthMiddlewareStack(URLRouter(websocket_urlpatterns)))

})
