# Generated by Django 2.1.3 on 2018-11-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20181107_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='based_on_profit',
            field=models.BooleanField(default=False, verbose_name='Calcular comissão baseado no lucro ?'),
        ),
    ]