# Generated by Django 2.1.3 on 2018-11-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20181119_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotation',
            name='is_updating',
            field=models.BooleanField(default=False, verbose_name='Impedir Mudança de Status?'),
        ),
    ]