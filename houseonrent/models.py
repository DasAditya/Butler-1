from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class House(models.Model):
    house_title = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    rent_price = models.IntegerField()
    advance_pymt = models.IntegerField()
    config = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    house_pic = models.CharField(max_length=1000)
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.house_title


class BookmarkHouse(models.Model):
    user = models.ForeignKey(User, default=1)
    house_title = models.CharField(max_length=200)
    address = models.CharField(max_length=1000)
    rent_price = models.IntegerField()
    advance_pymt = models.IntegerField()
    config = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    house_pic = models.CharField(max_length=1000)

    def __str__(self):
        return self.house_title


# class House(models.Model):
#     house_title = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     address = models.CharField(max_length=500)
#     size_bhk = models.CharField(max_length=50)
#     rent_price = models.CharField(max_length=50)
#     contact_no = models.IntegerField()
#     description = models.CharField(max_length=4000)
#     tenure = models.CharField(max_length=500)
#     sqft_area = models.IntegerField()
#     house_logo = models.FileField()
#
#     def __str__(self):
#         return self.house_title


class Picture(models.Model):
    house_thumb = models.CharField(max_length=1000)

    def __str__(self):
        return 'Pic ' + str(self.pk)

