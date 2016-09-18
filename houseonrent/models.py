from __future__ import unicode_literals

from django.db import models


class House(models.Model):
    house_title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    contact_no = models.IntegerField()
    size_bhk = models.CharField(max_length=50)
    rent_price = models.CharField(max_length=50)
    description = models.CharField(max_length=4000)
    tenure = models.CharField(max_length=500)
    sqft_area = models.IntegerField()
    house_logo = models.FileField()

    def __str__(self):
        return self.house_title


class Picture(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    pic_logo = models.FileField()
