# Generated by Django 2.0.1 on 2018-01-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180114_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reward',
            name='value',
            field=models.FloatField(default=0),
        ),
    ]