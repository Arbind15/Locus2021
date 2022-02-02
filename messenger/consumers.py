import json
from channels.generic.websocket import WebsocketConsumer
import time
from asgiref.sync import async_to_sync
from .models import Chat, ChatBody

class ChatList(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(10):
            self.send(text_data=f"{i}")

    def disconnect(self, close_code):
        print("disc")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': text_data_json
        }))

class ChatDetails(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(10):
            self.send(text_data=f"{i}")

    def disconnect(self, close_code):
        print("disc")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': text_data_json
        }))

class ChatUpdates(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        print("disconnected")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        chat_unit={
            "user":text_data_json['user'],
            "hospital": text_data_json['hospital'],
            "content": text_data_json['content'],
        }
        self.send(text_data=json.dumps({
            'message': chat_unit
        }))


class ChatUpdatesTmp(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # print(self.channel_layer)
        # # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        print("disconnected")

    def receive(self, text_data):
        text_data_json = json.loads(text_data)

        user=text_data_json['user']
        hospital= text_data_json['hospital']
        content=text_data_json['content']

        # self.send(text_data=json.dumps({
        #     'message': chat_unit
        # }))

        chat=Chat.objects.get(user=user,hospital=hospital)
        chat_body=ChatBody(Chat=chat,Chat_Content=content)

    def send_update(self,event):
        # print('here')
        self.send(json.dumps(event))