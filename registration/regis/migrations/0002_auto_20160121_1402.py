# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='college_name',
            field=models.CharField(default=b'JSS', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='course',
            field=models.CharField(default=b'Btech', max_length=10, choices=[(b'Btech', b'Btech'), (b'MBA', b'MBA'), (b'MAM', b'MAM'), (b'MCA', b'MCA')]),
        ),
    ]
