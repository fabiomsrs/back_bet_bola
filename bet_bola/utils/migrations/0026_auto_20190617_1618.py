# Generated by Django 2.2.2 on 2019-06-17 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0025_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='release',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 17, 16, 18, 4), verbose_name='Data da Aposta'),
        ),
    ]