# Generated by Django 2.1.7 on 2019-02-22 03:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20190222_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='create_table',
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 3, 31, 44, 520947, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 3, 31, 44, 520947, tzinfo=utc)),
        ),
    ]
