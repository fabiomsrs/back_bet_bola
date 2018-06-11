# Generated by Django 2.0.6 on 2018-06-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20180609_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betticket',
            name='bet_ticket_status',
            field=models.CharField(choices=[('Aguardando Resultados', 'Aguardando Resultados'), ('Não Venceu', 'Não Venceu'), ('Venceu', 'Venceu')], default='Aguardando Resultados', max_length=80, verbose_name='Status de Ticket'),
        ),
    ]
