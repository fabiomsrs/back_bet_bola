# Generated by Django 2.2.3 on 2019-07-15 14:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0026_auto_20190712_0951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='limit_time_to_cancel',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(45)], verbose_name='Tempo Limite de Cancelamento'),
        ),
    ]
