from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class UserDetail(models.Model):
    '''
    It stores the information about the users of the system.
    '''
    # List of year
    YEAR = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
    )

    # List of branches
    CSE = 'CSE'
    IT = 'IT'
    EE = 'EE'
    ECE = 'ECE'
    EEE = 'EEE'
    CE = 'CE'
    IC = 'IC'
    ME = 'ME'
    MT = 'MT'

    BRANCH = (
        (CSE, 'Computer Science and Engineering'),
        (IT, 'Information Technology'),
        (EE, 'Electrical Engineering'),
        (ECE, 'Electronics and Communication Engineering'),
        (EEE, 'Electrical and Electronics Engineering'),
        (CE, 'Civil Engineering'),
        (IC, 'Instrumentation and Control Engineering'),
        (ME, 'Mechanical Engineering'),
        (MT, 'Manufacturing Technology'),
    )

    user = models.OneToOneField(User)
    contact_no = models.CharField(max_length=10, blank=False, null=False)
    college_society = models.CharField(max_length=200, blank=False, null=False)
    year = models.PositiveIntegerField(null=False, blank=False, default=3,
                                       validators=[MinValueValidator(0),
                                                   MaxValueValidator(4)])
    branch = models.CharField(max_length=5, choices=BRANCH, null=False, blank=False)
    univ_roll_no = models.CharField(max_length=10, blank=False, null=False)
