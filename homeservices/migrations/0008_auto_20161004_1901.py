# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-04 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeservices', '0007_auto_20161004_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmarkhomeservices',
            name='close_time',
            field=models.CharField(default='2000', max_length=1000, null=True),
        ),
    ]