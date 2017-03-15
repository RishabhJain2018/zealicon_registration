from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Transaction(models.Model):
    username=models.OneToOneField(User)
    society=models.EmailField(max_length=200,null=True)
    jss_registration=models.CharField(max_length=10, null=True)
    other_registration=models.CharField(max_length=10,null=True)
    amount=models.CharField(max_length=10,null=True)
