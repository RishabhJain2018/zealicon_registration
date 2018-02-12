# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20170315_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='username',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
