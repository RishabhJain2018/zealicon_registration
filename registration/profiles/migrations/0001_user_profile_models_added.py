# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_no', models.CharField(max_length=10)),
                ('college_society', models.CharField(max_length=200)),
                ('year', models.PositiveIntegerField(default=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('branch', models.CharField(max_length=5, choices=[(b'CSE', b'Computer Science and Engineering'), (b'IT', b'Information Technology'), (b'EE', b'Electrical Engineering'), (b'ECE', b'Electronics and Communication Engineering'), (b'EEE', b'Electrical and Electronics Engineering'), (b'CE', b'Civil Engineering'), (b'IC', b'Instrumentation and Control Engineering'), (b'ME', b'Mechanical Engineering'), (b'MT', b'Manufacturing Technology')])),
                ('univ_roll_no', models.CharField(max_length=10)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
