# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_transaction_table_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='jss_registration',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='other_registration',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='society',
            field=models.EmailField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
