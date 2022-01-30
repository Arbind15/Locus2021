from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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