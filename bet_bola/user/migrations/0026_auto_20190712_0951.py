# Generated by Django 2.2.3 on 2019-07-12 09:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0025_auto_20190705_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='limit_time_to_cancel',
            field=models.IntegerField(blank=True, default=5, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(45)], verbose_name='Tempo Limite de Cancelamento'),
        ),
    ]
