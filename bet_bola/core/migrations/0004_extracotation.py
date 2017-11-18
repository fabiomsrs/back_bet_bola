# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-18 04:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_cotation_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraCotation',
            fields=[
                ('cotation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Cotation')),
            ],
            bases=('core.cotation',),
        ),
    ]