# Generated by Django 2.2.2 on 2019-06-06 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0021_auto_20190603_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='managercomission',
            name='profit_comission',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=30, verbose_name='Comissão do lucro'),
        ),
    ]
