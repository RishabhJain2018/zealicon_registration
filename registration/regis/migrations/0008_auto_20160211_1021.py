# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0007_auto_20160129_1359'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_Details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='participants_details',
            name='college_name',
            field=models.CharField(default=b'JSS', max_length=200, blank=True),
        ),
    ]
