from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# class Chat(models.Model):
#     user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
#     hospital=models.OneToOneField(User,on_delete=models.DO_NOTHING)
#     Date=models.DateField(default=timezone.now())
#     Chat_Body=models.TextField()
#     Remarks=models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'{self.user.username} -Chat'