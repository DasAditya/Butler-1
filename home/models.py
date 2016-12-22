from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class OTP(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    otp_assigned=models.IntegerField(null=True)
    otp_entered=models.IntegerField(null=True)
    otp_verified=models.NullBooleanField(default=False, null=True)

    def __str__(self):
        return self.user.username
