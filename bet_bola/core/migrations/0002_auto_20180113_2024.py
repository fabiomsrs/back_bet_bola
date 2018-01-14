# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-13 22:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betticket',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Payment'),
        ),
        migrations.AlterField(
            model_name='betticket',
            name='reward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Reward'),
        ),
    ]
