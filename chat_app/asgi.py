from channels.routing import URLRouter,ProtocolTypeRouter
from app.routing import websocket_urlpatterns
import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_app.settings')

application = ProtocolTypeRouter({
'http':get_asgi_application(),
'websocket':AuthMiddlewareStack(

URLRouter(
websocket_urlpatterns
)
)

})
