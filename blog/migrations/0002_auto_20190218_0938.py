# Generated by Django 2.1.7 on 2019-02-18 02:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_table',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 2, 38, 11, 912954, tzinfo=utc)),
        ),
    ]
