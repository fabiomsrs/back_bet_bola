# Generated by Django 2.1.7 on 2019-03-23 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_merge_20190321_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='cc',
            field=models.CharField(default='inter', max_length=5, verbose_name='CC'),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_status',
            field=models.IntegerField(choices=[(0, 'Não Iniciado'), (1, 'Ao Vivo'), (2, 'A ser corrigido'), (3, 'Terminado'), (4, 'Adiado'), (5, 'Cancelado'), (6, 'W.O'), (7, 'Interrompido'), (8, 'Abandonado'), (9, 'Retirado'), (99, 'Removido')], verbose_name='Status do Jogo'),
        ),
    ]