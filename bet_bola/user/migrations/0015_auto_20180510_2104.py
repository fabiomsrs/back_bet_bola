# Generated by Django 2.0.1 on 2018-05-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_auto_20180506_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='address',
            field=models.CharField(max_length=75, null=True, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='manager',
            name='cpf',
            field=models.CharField(max_length=11, null=True, verbose_name='CPF'),
        ),
    ]