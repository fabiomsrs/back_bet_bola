# Generated by Django 2.0.6 on 2018-07-05 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0034_auto_20180623_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='can_cancel_ticket',
            field=models.BooleanField(default=False, verbose_name='Cancela Ticket ?'),
        ),
        migrations.AddField(
            model_name='seller',
            name='limit_time_to_cancel',
            field=models.FloatField(default=5, verbose_name='Tempo Limite de Cancelamento'),
        ),
    ]