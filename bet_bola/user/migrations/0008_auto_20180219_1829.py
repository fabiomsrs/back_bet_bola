# Generated by Django 2.0.1 on 2018-02-19 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20180219_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seller',
            options={'permissions': (('be_seller', 'Be a seller, permission.'),), 'verbose_name': 'Vendedor', 'verbose_name_plural': 'Vendedores'},
        ),
    ]
