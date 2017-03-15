from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ParticipantsDetail(models.Model):
    name=models.CharField(max_length=200,blank=False,null=False)
    email=models.EmailField(max_length=200,blank=False,unique=True)
    course=models.CharField(max_length=10,blank=False)
    branch=models.CharField(max_length=10,blank=True,null=True)
    contact=models.CharField(max_length=10,blank=False,unique=True)
    college=models.CharField(max_length=200,blank=False,null=False)
    year=models.CharField(max_length=200)
    zeal_id= models.CharField(max_length=200)
    fee=models.IntegerField()
    id_card_print=models.BooleanField(default=False)
    receipt_print=models.BooleanField(default=False)
    created_by=models.ForeignKey(User)


class ParticipantsOnline(models.Model):
    zeal_id_temp=models.CharField(max_length=200,null=False)
    name=models.CharField(max_length=200,null=False)
    email=models.EmailField(max_length=200,null=False)
    course=models.CharField(max_length=200,null=False)
    branch=models.CharField(max_length=200,null=True,blank=True)
    contact=models.CharField(max_length=10,null=False)
    college=models.CharField(max_length=200,null=False)
    year=models.CharField(max_length=200,null=False)


class SearchOnline(models.Model):
    search=models.CharField(max_length=200,blank=False)
