# Generated by Django 2.0.6 on 2018-06-14 09:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0007_auto_20180613_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='punterpayedhistory',
            name='is_closed',
        ),
        migrations.AddField(
            model_name='punterpayedhistory',
            name='is_closed_for_manager',
            field=models.BooleanField(default=False, verbose_name='Gerente Prestou Conta?'),
        ),
        migrations.AddField(
            model_name='punterpayedhistory',
            name='is_closed_for_seller',
            field=models.BooleanField(default=False, verbose_name='Vendedor Prestou Conta?'),
        ),
        migrations.AlterField(
            model_name='revenuehistorymanager',
            name='actual_comission',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Comissão'),
        ),
        migrations.AlterField(
            model_name='revenuehistorymanager',
            name='earned_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Valor Recebido'),
        ),
        migrations.AlterField(
            model_name='revenuehistorymanager',
            name='final_revenue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Faturamento'),
        ),
        migrations.AlterField(
            model_name='revenuehistoryseller',
            name='actual_comission',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Comissão'),
        ),
        migrations.AlterField(
            model_name='revenuehistoryseller',
            name='earned_value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Valor Recebido'),
        ),
        migrations.AlterField(
            model_name='revenuehistoryseller',
            name='final_revenue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Faturamento'),
        ),
        migrations.AlterField(
            model_name='sellersaleshistory',
            name='bet_ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.BetTicket', verbose_name='Ticket Pago'),
        ),
    ]
