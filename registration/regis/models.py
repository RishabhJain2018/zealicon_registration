from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Participants_Details(models.Model):
	''' Registration models ''' 
	CSE ='CSE'
	IT = 'IT'
	EE = 'EE'
	ECE='ECE'
	CE='CE'
	IC='IC'
	ME='ME'
	MT='MT'
	BRANCH= (
		(CSE, 'Computer Science and Engineering' ),
		(IT, 'Information Technology' ),
		(EE, 'Electrical Engineering' ),
		(ECE, 'Electronics and Communication Engineering' ),
		(CE, 'Civil Engineering' ),
		(IC, 'Instrumentation and Control Engineering' ),
		(ME, 'Mechanical Engineering' ),
		(MT, 'Manufacturing Technology' ),
		)

	Btech='Btech'
	MBA='MBA'
	MAM='MAM'
	MCA='MCA'
	Mtech='Mtech'
	COURSE=(
		(Btech, 'Btech'),
		(MBA,'MBA'),
		(MAM,'MAM'),
		(MCA,'MCA'),
		(Mtech,'Mtech')
		)

	JSS='JSS'
	OTHER='OTHER'
	COLLEGE=(
		(JSS,'JSS'),
		(OTHER,'OTHER'),
		)

	FIRST='FIRST'
	SECOND='SECOND'
	THIRD='THIRD'
	FOURTH='FOURTH'
	YEAR=(
		(FIRST,'FIRST'),
		(SECOND,'SECOND'),
		(THIRD,'THIRD'),
		(FOURTH,'FOURTH'),

		)

	name=models.CharField(max_length=200,blank=True)
	email=models.EmailField(max_length=200,default=None, blank=False,unique=True)
	course=models.CharField(max_length=10,choices=COURSE,default=None,blank=True)
	branch=models.CharField(max_length=10,choices=BRANCH,blank=True,null=True, default=None)
	contact=models.CharField(max_length=10,blank=False,unique=True)
	college=models.CharField(max_length=200,choices=COLLEGE,blank=True,null=True)
	college_name=models.CharField(max_length=200,blank=True,null=False, default=JSS)
	year=models.CharField(max_length=200,choices=YEAR,default=FIRST)

	