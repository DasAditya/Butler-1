from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Furniture(models.Model):
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    place_id = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    contact = models.CharField(max_length=100, null=True)
    open_now = models.CharField(max_length=1000, null=True, default='True')
    open_time = models.CharField(max_length=1000, null=True, default='1000')
    close_time = models.CharField(max_length=1000, null=True, default='2000')
    rating = models.CharField(max_length=1000, null=True, default='3')
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BookmarkFurniture(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    latitude = models.FloatField(null=True,default=1.0)
    longitude = models.FloatField(null=True,default=1.0)
    place_id = models.CharField(max_length=1000)
    img = models.CharField(max_length=1000)
    contact = models.CharField(max_length=100, null=True,default='1')
    open_now = models.CharField(max_length=1000, null=True,default='1000')
    open_time = models.CharField(max_length=1000, null=True,default='1000')
    close_time = models.CharField(max_length=1000, null=True,default='2000')
    rating = models.CharField(max_length=1000, null=True, default='Null')

    def __str__(self):
        return self.name


class Picture(models.Model):
    homeservices_thumb = models.CharField(max_length=1000)

    def __str__(self):
        return 'Pic ' + str(self.pk)

