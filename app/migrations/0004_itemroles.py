# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-05 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170123_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
