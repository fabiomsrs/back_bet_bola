# Generated by Django 2.0.1 on 2018-05-12 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_betticket_cotation_value_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='CotationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nome da Cota')),
                ('original_value', models.FloatField(default=0, verbose_name='Valor Original')),
                ('value', models.FloatField(default=0, verbose_name='Valor Modificado')),
                ('winning', models.NullBooleanField(verbose_name='Vencedor ?')),
                ('is_standard', models.BooleanField(default=False, verbose_name='Cota Padrão ?')),
                ('total', models.FloatField(blank=True, null=True)),
                ('bet_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotations_history', to='core.BetTicket', verbose_name='Ticket')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cotations_history', to='core.Game', verbose_name='Jogo')),
                ('kind', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cotations_history', to='core.Market', verbose_name='Tipo da Cota')),
            ],
        ),
    ]