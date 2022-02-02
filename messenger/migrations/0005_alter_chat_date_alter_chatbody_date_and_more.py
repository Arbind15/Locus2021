# Generated by Django 4.0.1 on 2022-02-02 06:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0004_alter_chat_date_alter_chat_hospital_alter_chat_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 12, 34, 46, 402259)),
        ),
        migrations.AlterField(
            model_name='chatbody',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 2, 12, 34, 46, 402259)),
        ),
        migrations.AlterField(
            model_name='chatbody',
            name='Sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='message_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]