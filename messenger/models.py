from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from c


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

        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.Chat.user.username}-{self.Chat.hospital.username}'
