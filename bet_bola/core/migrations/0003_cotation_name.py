# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-13 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171113_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotation',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
