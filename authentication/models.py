from django.db import models
import sqlite3, time
from django.contrib.auth.models import User
from PIL import Image
import datetime
from django.utils import timezone


class userProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='username', primary_key=True)
    Citizenship_Number = models.CharField(max_length=50, default="")
    DOB = models.DateField()
    Date = models.DateField(default=timezone.now())
    # Address = models.CharField(max_length=500)
    # Profile_Picture = models.ImageField(default="default.jpg", upload_to='user_pics')
    # Citizen_Front = models.ImageField(default="default.jpg", upload_to='ctzn_pics')
    # Citizen_Rear = models.ImageField(default="default.jpg", upload_to='ctzn_pics')
    Health_Stat = models.BooleanField(default=False)
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -userProfile'

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     img1 = Image.open(self.Profile_Picture.path)
    #     img1.thumbnail((200, 200))
    #     img1.save(self.Profile_Picture.path)
    #     img1 = Image.open(self.Citizen_Front.path)
    #     img1.thumbnail((500, 500))
    #     img1.save(self.Citizen_Front.path)
    #     img1 = Image.open(self.Citizen_Rear.path)
    #     img1.thumbnail((500, 500))
    #     img1.save(self.Citizen_Rear.path)


class userStatus(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='userStatus', primary_key=True)
    First_Dose_Date = models.CharField(default='',max_length=100)
    Second_Dose_Date = models.CharField(default='',max_length=100)
    New_Vaccine_Request = models.BooleanField(default=False)
    New_Vaccine_Location = models.CharField(default='',max_length=500)
    Current_PCR = models.BooleanField(default=False)
    Schedule_Stat=models.BooleanField(default=False)
    Date = models.DateTimeField(default=datetime.datetime.now())
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -Status'


class hospitalProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='hospital', primary_key=True)
    Phone_Number = models.CharField(max_length=14, default="")
    Date = models.DateField(default=timezone.now())
    Address = models.CharField(max_length=500)
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -hospitalProfile'


class adminProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='hospital', primary_key=True)
    Citizenship_Number = models.CharField(max_length=50, default='')
    Date = models.DateField(default=timezone.now())
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -adminProfile'


class hospitalStatus(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='hospitalStatus', primary_key=True)
    Vaccine_Code = models.CharField(max_length=100)
    Date = models.DateField(default=timezone.now())
    Total_Assigned_Vaccine = models.IntegerField(default=0)
    Used_Vaccine = models.IntegerField(default=0)
    Remarks = models.TextField(max_length=100, default="")

    def __str__(self):
        return f'{self.username.username} -Status'
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

