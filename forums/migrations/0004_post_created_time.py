# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-06 01:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_auto_20161006_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
