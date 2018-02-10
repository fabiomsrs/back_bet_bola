# Generated by Django 2.0.1 on 2018-01-21 10:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180119_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='betticket',
            name='bet_ticket_status',
            field=models.CharField(choices=[('Aguardando Resultados', 'Aguardando Resultados'), ('Não Venceu', 'Não Venceu'), ('Venceu', 'Venceu')], default='Aguardando Resultados', max_length=80, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='betticket',
            name='cotations',
            field=models.ManyToManyField(related_name='bet_ticket', to='core.Cotation', verbose_name='Cota'),
        ),
        migrations.AlterField(
            model_name='betticket',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data da aposta'),
        ),
        migrations.AlterField(
            model_name='betticket',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Payment', verbose_name='Pagamento'),
        ),
        migrations.AlterField(
            model_name='betticket',
            name='random_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.RandomUser', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='betticket',
            name='reward',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Reward', verbose_name='Recompensa'),
        ),
        migrations.AlterField(
            model_name='betticket',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='my_bet_tickets', to=settings.AUTH_USER_MODEL, verbose_name='Apostador'),
        ),
        migrations.AlterField(
            model_name='betticket',
            name='value',
            field=models.FloatField(verbose_name='Apostado'),
        ),
        migrations.AlterField(
            model_name='championship',
            name='country',
            field=models.CharField(max_length=45, verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='championship',
            name='name',
            field=models.CharField(help_text='Campeonato', max_length=80, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotations', to='core.Game', verbose_name='Jogo'),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='is_standard',
            field=models.BooleanField(default=False, verbose_name='Cota Padrão ?'),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='kind',
            field=models.CharField(max_length=100, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nome da Cota'),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='original_value',
            field=models.FloatField(default=0, verbose_name='Valor Original'),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='value',
            field=models.FloatField(default=0, verbose_name='Valor Modificado'),
        ),
        migrations.AlterField(
            model_name='cotation',
            name='winning',
            field=models.NullBooleanField(verbose_name='Vencedor ?'),
        ),
        migrations.AlterField(
            model_name='game',
            name='championship',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_games', to='core.Championship', verbose_name='Campeonato'),
        ),
        migrations.AlterField(
            model_name='game',
            name='ft_score',
            field=models.CharField(max_length=80, null=True, verbose_name='Placar no final do Jogo'),
        ),
        migrations.AlterField(
            model_name='game',
            name='ht_score',
            field=models.CharField(max_length=80, null=True, verbose_name='Placar até o meio-tempo'),
        ),
        migrations.AlterField(
            model_name='game',
            name='local_team_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Placar Time de Casa'),
        ),
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Nome do Jogo'),
        ),
        migrations.AlterField(
            model_name='game',
            name='start_game_date',
            field=models.DateTimeField(verbose_name='Início da Partida'),
        ),
        migrations.AlterField(
            model_name='game',
            name='status_game',
            field=models.CharField(choices=[('NS', 'Não Iniciado'), ('LIVE', 'Ao Vivo'), ('HT', 'Meio Tempo'), ('FT', 'Tempo Total'), ('ET', 'Tempo Extra'), ('PEN_LIVE', 'Penaltis'), ('AET', 'Terminou após tempo extra'), ('BREAK', 'Esperando tempo extra'), ('FT_PEN', 'Tempo total após os penaltis'), ('CANCL', 'Cancelado'), ('POSTP', 'Adiado'), ('INT', 'Interrompindo'), ('ABAN', 'Abandonado'), ('SUSP', 'Suspendido'), ('AWARDED', 'Premiado'), ('DELAYED', 'Atrasado'), ('TBA', 'A ser anunciado'), ('WO', 'WO')], default='Não Iniciado', max_length=80, verbose_name='Status do Jogo'),
        ),
        migrations.AlterField(
            model_name='game',
            name='visitor_team_score',
            field=models.IntegerField(blank=True, null=True, verbose_name='Placar do Visitante'),
        ),
    ]