# Generated by Django 2.2.2 on 2019-06-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0014_auto_20190607_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='closed_for_manager',
            field=models.BooleanField(default=False, verbose_name='Disponível?'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='closed_for_seller',
            field=models.BooleanField(default=False, verbose_name='Disponível?'),
        ),
    ]
