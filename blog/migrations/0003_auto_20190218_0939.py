# Generated by Django 2.1.7 on 2019-02-18 02:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190218_0938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_table',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 18, 2, 39, 33, 589392, tzinfo=utc)),
        ),
    ]
