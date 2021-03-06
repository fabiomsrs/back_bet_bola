# Generated by Django 2.1.3 on 2019-03-13 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerTransactions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(auto_now_add=True, verbose_name='Data da Transação')),
                ('transferred_amount', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Valor Transferido')),
                ('manager_before_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Saldo Anterior')),
                ('manager_after_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Saldo Atual')),
                ('seller_before_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Saldo Anterior(Cambista)')),
                ('seller_after_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Saldo Atual(Cambista)')),
            ],
            options={
                'verbose_name': 'Transf. - Gerente',
                'verbose_name_plural': 'Transf. - Gerentes',
            },
        ),
        migrations.CreateModel(
            name='PunterPayedHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('punter_payed', models.CharField(max_length=200, verbose_name='Apostador')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='Data do Pagamento')),
                ('payed_value', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Valor Pago')),
                ('is_closed_for_seller', models.BooleanField(default=False, verbose_name='Cambista Prestou Conta?')),
                ('is_closed_for_manager', models.BooleanField(default=False, verbose_name='Cambista Prestou Conta?')),
            ],
            options={
                'verbose_name': 'Pag. - Apostador',
                'verbose_name_plural': 'Pag. - Apostadores',
            },
        ),
        migrations.CreateModel(
            name='RevenueHistoryManager',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('who_reseted_revenue', models.CharField(max_length=200, verbose_name='Reponsável pelo Fechamento')),
                ('revenue_reseted_date', models.DateTimeField(auto_now_add=True, verbose_name='Data da Transação')),
                ('final_revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Entrada Total')),
                ('actual_comission', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='% Comissão')),
                ('earned_value', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Comissão')),
                ('final_out_value', models.DecimalField(blank=True, decimal_places=2, max_digits=40, null=True, verbose_name='Saída Total')),
                ('profit', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Lucro')),
            ],
            options={
                'verbose_name': 'Pag. - Gerente',
                'verbose_name_plural': 'Pag. - Gerentes',
            },
        ),
        migrations.CreateModel(
            name='RevenueHistorySeller',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('who_reseted_revenue', models.CharField(max_length=200, verbose_name='Reponsável pelo Fechamento')),
                ('revenue_reseted_date', models.DateTimeField(auto_now_add=True, verbose_name='Data da Transação')),
                ('final_revenue', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Entrada Total')),
                ('earned_value', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Comissão')),
                ('final_out_value', models.DecimalField(blank=True, decimal_places=2, max_digits=40, null=True, verbose_name='Saída Total')),
                ('profit', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Lucro')),
            ],
            options={
                'verbose_name': 'Pag. - Cambista',
                'verbose_name_plural': 'Pag. - Cambistas',
            },
        ),
        migrations.CreateModel(
            name='SellerSalesHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_date', models.DateTimeField(auto_now_add=True, verbose_name='Data da Venda')),
                ('value', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Valor Apostado')),
                ('seller_before_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Saldo Anterior')),
                ('seller_after_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True, verbose_name='Saldo Atual')),
            ],
            options={
                'verbose_name': 'Entrada - Cambista',
                'verbose_name_plural': 'Entradas - Cambistas',
            },
        ),
        migrations.CreateModel(
            name='TicketCancelationHistory',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('who_cancelled', models.CharField(max_length=200, verbose_name='Quem Cancelou ?')),
                ('cancelation_date', models.DateTimeField(auto_now_add=True, verbose_name='Data do Cancelamento')),
            ],
            options={
                'verbose_name': 'Can. - Bilhete',
                'verbose_name_plural': 'Can. - Tickets',
            },
        ),
    ]
