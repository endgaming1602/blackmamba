# Generated by Django 2.1.7 on 2019-02-22 03:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190222_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 3, 33, 40, 734518, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 22, 3, 33, 40, 734518, tzinfo=utc)),
        ),
    ]