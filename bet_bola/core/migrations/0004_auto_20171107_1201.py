# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-07 15:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_cotation_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betticket',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
    ]
