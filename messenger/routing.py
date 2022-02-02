from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'messages/chatlist/', consumers.ChatList.as_asgi()),
    re_path(r'messages/chatdetails/', consumers.ChatDetails.as_asgi()),
    re_path(r'messages/chatupdate/', consumers.ChatUpdates.as_asgi()),

    re_path(r'messages/chatupdatetmp/(?P<room_name>\w+)/', consumers.ChatUpdatesTmp.as_asgi()),
]
