# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regis', '0003_auto_20160122_1840'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Participants_Details',
        ),
    ]
