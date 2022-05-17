from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Organisation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='org')
    org_name = models.CharField(max_length=5000,blank=True,null=True)


class StoreBuyer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='str_name')
    store_name = models.CharField(max_length=5000,blank=True,null=True)