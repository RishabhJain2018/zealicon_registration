from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class ParticipantsDetail(models.Model):
	''' Registration models ''' 

	name=models.CharField(max_length=200,blank=False,null=False)
	email=models.EmailField(max_length=200,blank=False,unique=True)
	course=models.CharField(max_length=10,blank=False)
	branch=models.CharField(max_length=10,blank=True,null=True)
	contact=models.CharField(max_length=10,blank=False,unique=True)
	college=models.CharField(max_length=200,blank=False,null=False)
	year=models.CharField(max_length=200)
	zeal_id_final = models.CharField(max_length=200)
	fee=models.IntegerField()
	id_card=models.IntegerField(default=0)
	receipt=models.IntegerField(default=0)


class ParticipantsOnline(models.Model):
	zealid=models.CharField(max_length=200)
	name=models.CharField(max_length=200)
	email=models.EmailField(max_length=200)
	course=models.CharField(max_length=200)
	branch=models.CharField(max_length=200)
	contact=models.CharField(max_length=10)
	college=models.CharField(max_length=200)
	year=models.CharField(max_length=200)

