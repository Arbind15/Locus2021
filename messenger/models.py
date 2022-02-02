from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='user')
    hospital = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='hospital')
    Date = models.DateTimeField(default=datetime.datetime.now())
    Remarks = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.user.username}-{self.hospital.username}'


class ChatBody(models.Model):
    Chat = models.ForeignKey(Chat, on_delete=models.DO_NOTHING, related_name='chat_body')
    Sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='message_sender')
    Chat_Content = models.TextField(default="")
    Date = models.DateTimeField(default=datetime.datetime.now())
    Seen_Status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        data = {
            "Sender": str(self.Sender),
            "Content":str(self.Chat_Content),
            "Date": str(self.Date),
            "Seen_Status": str(self.Seen_Status)
        }
        # print(channel_layer)
        async_to_sync(channel_layer.group_send)(
            "chat_arbind",
            {
                "type": 'send_update',
                "value": data
            }
        )
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.Chat.user.username}-{self.Chat.hospital.username}'
