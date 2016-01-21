from django.db import models

# Create your models here.
class Register(models.Model):
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
	COURSE=(
		(Btech, 'Btech'),
		(MBA,'MBA'),
		(MAM,'MAM'),
		(MCA,'MCA'),
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


	name=models.CharField(max_length=200,blank=False)
	email=models.EmailField(default=None, blank=False,unique=True)
	course=models.CharField(max_length=10,choices=COURSE,default=Btech)
	branch=models.CharField(max_length=10,choices=BRANCH,blank=True,default=None,null=True)
	contact=models.CharField(max_length=10,blank=False,unique=True)
	college=models.CharField(max_length=10,choices=COLLEGE,default=JSS)
	college_name=models.CharField(max_length=200,blank=True,default=JSS,null=True)
	year=models.CharField(max_length=1,choices=YEAR,default=FIRST)