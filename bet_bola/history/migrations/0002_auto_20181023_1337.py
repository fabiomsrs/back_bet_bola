# Generated by Django 2.1.2 on 2018-10-23 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketcancelationhistory',
            name='cancelation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data do Cancelamento'),
        ),
    ]
