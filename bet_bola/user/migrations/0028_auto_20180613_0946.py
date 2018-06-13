# Generated by Django 2.0.6 on 2018-06-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_auto_20180612_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Comissão'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='credit_limit_to_add',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Crédito'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='commission',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Comissão'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='credit_limit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30, verbose_name='Créditos'),
        ),
    ]
