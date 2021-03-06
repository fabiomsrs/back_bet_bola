# Generated by Django 2.2.2 on 2019-06-07 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0013_reward_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(0, 'Aguardando Resultados'), (1, 'Não Venceu'), (2, 'Venceu, Ganhador Pago'), (3, 'Venceu, Bilhete não Pago'), (4, 'Venceu, Prestar Contas'), (5, 'Cancelado'), (6, 'Reebolsado')], default=0, verbose_name='Status do Ticket'),
        ),
    ]
