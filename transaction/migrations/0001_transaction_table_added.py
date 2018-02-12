# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('society', models.EmailField(unique=True, max_length=200)),
                ('jss_registration', models.CharField(max_length=10)),
                ('other_registration', models.CharField(max_length=10, null=True, blank=True)),
                ('amount', models.CharField(unique=True, max_length=10)),
            ],
        ),
    ]
