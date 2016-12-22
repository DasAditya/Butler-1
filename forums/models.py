from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Topic(models.Model):
    user = models.ForeignKey(User, default=1)
    title = models.TextField(max_length=1000)
    category = models.TextField(max_length=100)
    no_of_posts = models.IntegerField(default=0)
    created_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return  self.title


class Post(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    msg = models.TextField(max_length=10000)
    created_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.topic + '-' + self.user.username
