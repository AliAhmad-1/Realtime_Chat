from django.urls import path,re_path
from . import consumers

websocket_urlpatterns=[
path('ws/awc/group_chat/<str:group_name>/',consumers.MyAsyncWebsocketConsumer.as_asgi()),
path('ws/awc/person_chat/<int:id>/',consumers.AsyncPersonChatConsumer.as_asgi()),
path('ws/awc/online/',consumers.AsyncOnlineConsumer.as_asgi()),
path('ws/awc/send_notification/',consumers.SendNotification.as_asgi()),
]