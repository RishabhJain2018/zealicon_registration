# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0008_auto_20160211_1021'),
    ]

    operations = [
        migrations.DeleteModel(
            name='College_Details',
        ),
        migrations.RemoveField(
            model_name='participants_details',
            name='college_name',
        ),
        migrations.AlterField(
            model_name='participants_details',
            name='college',
            field=models.CharField(default=b'JSS Academy of Technical Education', max_length=200),
        ),
    ]
