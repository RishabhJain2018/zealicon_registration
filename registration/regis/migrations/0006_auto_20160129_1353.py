# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0005_auto_20160129_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants_details',
            name='college_name',
            field=models.CharField(default=b'JSS', max_length=200, blank=True),
        ),
    ]
