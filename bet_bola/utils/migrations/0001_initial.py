# Generated by Django 2.0.6 on 2018-10-14 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simple', models.IntegerField(default=10, verbose_name='Apostas Simples')),
                ('double', models.IntegerField(default=10, verbose_name='Apostas Duplas')),
                ('triple_amount', models.IntegerField(default=10, verbose_name='Apostas Triplas')),
                ('four_plus_amount', models.IntegerField(default=10, verbose_name='Mais de 3')),
                ('seller_related', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comissions', to='user.Seller', verbose_name='Cambista Relacionado')),
            ],
            options={
                'verbose_name': 'Comissão do Cambista',
                'verbose_name_plural': 'Comissões dos Cambistas',
            },
        ),
        migrations.CreateModel(
            name='GeneralConfigurations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_cotation_value', models.DecimalField(decimal_places=2, default=200, max_digits=30, verbose_name='Valor Máximo das Cotas')),
                ('min_number_of_choices_per_bet', models.IntegerField(default=1, verbose_name='Número mínimo de escolhas por Aposta')),
                ('max_reward_to_pay', models.DecimalField(decimal_places=2, default=50000, max_digits=30, verbose_name='Valor máximo pago pela Banca')),
                ('min_bet_value', models.DecimalField(decimal_places=2, default=1, max_digits=30, verbose_name='Valor mínimo da aposta')),
                ('max_bet_value', models.DecimalField(decimal_places=2, default=1000000, max_digits=30, verbose_name='Valor máximo da aposta')),
                ('min_cotation_sum', models.DecimalField(decimal_places=2, default=1, max_digits=30, verbose_name='Valor mínimo da cota total')),
                ('max_cotation_sum', models.DecimalField(decimal_places=2, default=100000, max_digits=30, verbose_name='Valor máximo da cota total')),
                ('percentual_reduction', models.IntegerField(default=100, verbose_name='Redução Percentual')),
                ('auto_pay_punter', models.BooleanField(default=False, verbose_name='Auto Pagar Vencedores')),
            ],
            options={
                'verbose_name': 'Configurar Restrições',
                'verbose_name_plural': 'Configurar Restrições',
            },
        ),
        migrations.CreateModel(
            name='MarketReduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_to_reduct', models.IntegerField(choices=[(1, 'Vencedor do Encontro'), (10, 'Casa/Visitante'), (37, 'Vencedor do Primeiro Tempo'), (80, 'Vencedor do Segundo Tempo'), (976334, 'Resultado/Total de Gol(s)'), (975916, 'Resultado Exato no Primeiro Tempo'), (975909, 'Resultado Exato do Jogo'), (976241, 'Número Exato de Gol(s)'), (59, 'Os Dois Times Marcam'), (976360, 'Time Visitante Marca'), (976348, 'Time da Casa Marca'), (976096, 'Time da Casa NÃO Tomará Gol(s)'), (8594683, 'Time Visitante NÃO Tomará Gol(s)'), (976204, 'Total de Gols do Visitante'), (976198, 'Total de Gols da Casa'), (12, 'Total de Gol(s) no Encontro, Acima/Abaixo'), (47, 'Total de Gol(s) no Segundo Tempo, Acima/Abaixo'), (38, 'Total de Gols do Primeiro Tempo, Acima/Abaixo'), (976144, 'Etapa com Mais Gol(s)'), (976316, 'Resultado/2 Times Marcam'), (976193, 'Vencedor nas Duas Etapas'), (63, 'Dupla Chance'), (976236, 'Vencer e não tomar Gol(s)'), (975930, 'Placar Impar/Par')], unique=True, verbose_name='Tipo de Aposta')),
                ('reduction_percentual', models.IntegerField(default=100, verbose_name='Percentual de Redução')),
            ],
            options={
                'verbose_name': 'Redução',
                'verbose_name_plural': 'Reduções',
            },
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overview', models.BooleanField(default=True, verbose_name='Gerar Visão Geral')),
            ],
            options={
                'verbose_name': 'Visão Geral',
                'verbose_name_plural': 'Visão Geral',
            },
        ),
    ]
