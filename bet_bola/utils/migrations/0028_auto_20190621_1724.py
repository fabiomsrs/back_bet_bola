# Generated by Django 2.2.2 on 2019-06-21 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0027_auto_20190621_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='release',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 21, 17, 24, 2), verbose_name='Data da Aposta'),
        ),
    ]
