# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-05 14:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Championship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='championship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_games', to='core.Championship'),
        ),
    ]
