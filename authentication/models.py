from django.db import models
import sqlite3, time
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='username', primary_key=True)
    # Phone_Number = models.CharField(max_length=14, default="")
    DOB = models.DateField()
    Date = models.DateField(default=timezone.now())
    # Address = models.CharField(max_length=500)
    # Profile_Picture = models.ImageField(default="default.jpg", upload_to='user_pics')
    # Citizen_Front = models.ImageField(default="default.jpg", upload_to='ctzn_pics')
    # Citizen_Rear = models.ImageField(default="default.jpg", upload_to='ctzn_pics')
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img1 = Image.open(self.Profile_Picture.path)
        img1.thumbnail((200, 200))
        img1.save(self.Profile_Picture.path)
        img1 = Image.open(self.Citizen_Front.path)
        img1.thumbnail((500, 500))
        img1.save(self.Citizen_Front.path)
        img1 = Image.open(self.Citizen_Rear.path)
        img1.thumbnail((500, 500))
        img1.save(self.Citizen_Rear.path)

# class userStatus(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='userStatus', primary_key=True)
#     Date=models.DateField(timezone.now())
#     Symptoms=models.TextField()
#     Vitals=models.TextField()
#     Remarks = models.TextField(max_length=100, default="")
#
#     def __str__(self):
#         return f'{self.username.username} -Status'



class hospitalProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='hospital', primary_key=True)
    Phone_Number = models.CharField(max_length=14, default="")
    ESTD = models.DateField()
    Date = models.DateField(default=timezone.now())
    Address = models.CharField(max_length=500)
    Pan_Number = models.CharField(max_length=100, default="")
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -Profile'


# class hospitalStatus(models.Model):
#     username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='hospitalStatus', primary_key=True)
#     Date = models.DateField(default=timezone.now())
#     Total_Assigned_Vaccine = models.IntegerField(default=0)
#     Vaccine_Code = models.CharField(max_length=100)
#     Used_Vaccine = models.IntegerField(default=0)
#     Remarks = models.TextField(max_length=100, default="")
#
#     def __str__(self):
#         return f'{self.username.username} -Status'
#
# class Vaccination(models.Model):
#     user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
#     hospital=models.OneToOneField(User,on_delete=models.DO_NOTHING)
#     Date=models.DateField(default=timezone.now())
#     Vaccine_Code=models.CharField(max_length=100)
#     Dose_Type=models.IntegerField()
#     Remarks=models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'{self.user.username} -Vaccine'
#
#
# class Chat(models.Model):
#     user=models.OneToOneField(User,on_delete=models.DO_NOTHING)
#     hospital=models.OneToOneField(User,on_delete=models.DO_NOTHING)
#     Date=models.DateField(default=timezone.now())
#     Chat_Body=models.TextField()
#     Remarks=models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'{self.user.username} -Chat'

