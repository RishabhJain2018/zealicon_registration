# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0001_added_participant_created_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participantsonline',
            name='contact',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='participantsonline',
            name='email',
            field=models.EmailField(unique=True, max_length=200),
        ),
    ]
