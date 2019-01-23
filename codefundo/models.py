from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator,MaxLengthValidator
class user_details(models.Model):
    aadhar_no =models.IntegerField(default=0, unique=True)
    pincode   =models.IntegerField(default = 0)
    city  = models.CharField(max_length=20,default=None)

class track_users(models.Model):
    pincode = models.IntegerField( default=0,unique=True)
    user_count=models.IntegerField(default=0)
    city  = models.CharField(max_length=20,default=None)
    fund = models.IntegerField(default=0)

class gov_fund(models.Model):
    fund = models.IntegerField(default=0)
