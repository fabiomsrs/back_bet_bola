# Generated by Django 2.1.2 on 2018-11-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181023_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotation',
            name='id_string',
            field=models.CharField(default='', max_length=40),
        ),
    ]
