# Generated by Django 4.0.1 on 2022-02-03 09:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0007_alter_chat_date_alter_chatbody_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 3, 15, 17, 20, 800343)),
        ),
        migrations.AlterField(
            model_name='chatbody',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 3, 15, 17, 20, 801344)),
        ),
    ]