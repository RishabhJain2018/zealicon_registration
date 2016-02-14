# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0010_college'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants_details',
            name='college',
            field=models.CharField(default=None, max_length=200),
        ),
    ]
