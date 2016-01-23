# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0002_auto_20160121_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='branch',
            field=models.CharField(default=None, max_length=10, null=True, blank=True, choices=[(b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='college',
            field=models.CharField(blank=True, max_length=200, null=True, choices=[(b'JSS', b'JSS'), (b'OTHER', b'OTHER')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='college_name',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='course',
            field=models.CharField(default=b'Btech', max_length=10, blank=True, choices=[(b'Btech', b'Btech'), (b'MBA', b'MBA'), (b'MAM', b'MAM'), (b'MCA', b'MCA'), (b'Mtech', b'Mtech')]),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(default=None, unique=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='register',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='year',
            field=models.CharField(default=b'FIRST', max_length=200, choices=[(b'FIRST', b'FIRST'), (b'SECOND', b'SECOND'), (b'THIRD', b'THIRD'), (b'FOURTH', b'FOURTH')]),
        ),
    ]
