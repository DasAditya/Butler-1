from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=1000)
    location_address= models.CharField(max_length=1000)
    location_locality = models.CharField(max_length=1000)
    location_city = models.CharField(max_length=1000)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    restaurant_cuisine = models.CharField(max_length=1000)
    restaurant_avgcostfor2 = models.IntegerField()
    restaurant_thumb = models.CharField(max_length=1000)
    user_rating_agg = models.FloatField()
    user_rating_vote = models.FloatField()
    res_id = models.IntegerField()
    is_bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.restaurant_name


class BookmarkRest(models.Model):
    user = models.ForeignKey(User, default=1)
    restaurant_name = models.CharField(max_length=1000)
    location_address = models.CharField(max_length=1000)
    location_locality = models.CharField(max_length=1000)
    location_city = models.CharField(max_length=1000)
    location_latitude = models.FloatField()
    location_longitude = models.FloatField()
    restaurant_cuisine = models.CharField(max_length=1000)
    restaurant_avgcostfor2 = models.IntegerField()
    restaurant_thumb = models.CharField(max_length=1000)
    user_rating_agg = models.FloatField()
    user_rating_vote = models.FloatField()
    res_id = models.IntegerField()


    def __str__(self):
        return self.restaurant_name + '- bookmark'


