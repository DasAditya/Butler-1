# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-26 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houseonrent', '0005_house_house_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmarkhouse',
            name='house',
        ),
        migrations.RemoveField(
            model_name='bookmarkhouse',
            name='user',
        ),
        migrations.DeleteModel(
            name='BookmarkHouse',
        ),
    ]
