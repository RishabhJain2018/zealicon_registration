# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0011_auto_20160212_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participants_Online',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zealid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='College',
        ),
        migrations.AddField(
            model_name='participants_details',
            name='zealid_final',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='participants_details',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
