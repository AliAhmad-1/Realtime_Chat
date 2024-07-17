from channels.routing import URLRouter,ProtocolTypeRouter
from app.routing import websocket_urlpatterns
import os
import django
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')
django.setup()
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AllowedHostsOriginValidator(
    AuthMiddlewareStack(URLRouter(websocket_urlpatterns)))

})
