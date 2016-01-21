# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(default=None, unique=True, max_length=254)),
                ('course', models.CharField(default=b'BTech', max_length=10, choices=[(b'BTech', b'BTech'), (b'MBA', b'MBA'), (b'MAM', b'MAM'), (b'MCA', b'MCA')])),
                ('branch', models.CharField(default=None, max_length=10, choices=[(b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')])),
                ('contact', models.CharField(unique=True, max_length=10)),
                ('college', models.CharField(max_length=10, choices=[(b'JSS', b'JSS'), (b'OTHER', b'OTHER')])),
                ('college_name', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=1, choices=[(b'FIRST', b'FIRST'), (b'SECOND', b'SECOND'), (b'THIRD', b'THIRD'), (b'FOURTH', b'FOURTH')])),
            ],
        ),
    ]
