# Generated by Django 2.1.7 on 2019-02-22 03:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20190222_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 3, 34, 14, 235912, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 3, 34, 14, 235912, tzinfo=utc)),
        ),
    ]
