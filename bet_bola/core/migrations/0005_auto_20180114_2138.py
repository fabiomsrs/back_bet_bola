# Generated by Django 2.0.1 on 2018-01-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cotation_percentual_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cotation',
            name='percentual_value',
        ),
        migrations.AddField(
            model_name='cotation',
            name='original_value',
            field=models.FloatField(default=0),
        ),
    ]
