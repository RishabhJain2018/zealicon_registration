# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0004_auto_20160125_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participants_details',
            name='college_name',
            field=models.CharField(default=b'JSS', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participants_details',
            name='course',
            field=models.CharField(default=None, max_length=10, blank=True, choices=[(b'Btech', b'Btech'), (b'MBA', b'MBA'), (b'MAM', b'MAM'), (b'MCA', b'MCA'), (b'Mtech', b'Mtech')]),
        ),
    ]
