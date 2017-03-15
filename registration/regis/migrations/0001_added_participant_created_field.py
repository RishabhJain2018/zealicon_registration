# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantsDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(unique=True, max_length=200)),
                ('course', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10, null=True, blank=True)),
                ('contact', models.CharField(unique=True, max_length=10)),
                ('college', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('zeal_id', models.CharField(max_length=200)),
                ('fee', models.IntegerField()),
                ('id_card_print', models.BooleanField(default=False)),
                ('receipt_print', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantsOnline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zeal_id_temp', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200, null=True, blank=True)),
                ('contact', models.CharField(max_length=10)),
                ('college', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SearchOnline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('search', models.CharField(max_length=200)),
            ],
        ),
    ]
