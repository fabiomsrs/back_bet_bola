# Generated by Django 2.1 on 2018-09-27 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20180830_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='betticket',
            name='cotation_value_total',
        ),
    ]
