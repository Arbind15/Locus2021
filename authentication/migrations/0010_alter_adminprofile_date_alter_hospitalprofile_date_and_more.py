# Generated by Django 4.0.1 on 2022-02-01 08:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_userprofile_health_stat_alter_adminprofile_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminprofile',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 2, 1, 8, 54, 51, 340329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hospitalprofile',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 2, 1, 8, 54, 51, 340329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='hospitalstatus',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 2, 1, 8, 54, 51, 340329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 2, 1, 8, 54, 51, 340329, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userstatus',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 2, 1, 8, 54, 51, 340329, tzinfo=utc)),
        ),
    ]
