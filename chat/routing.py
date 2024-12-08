from django.urls import path
from . import consumer

websocket_urlpatterns = [
    path(r"ws/room/<str:room_name>/", consumer.ChatConsumer.as_asgi()),
    
]