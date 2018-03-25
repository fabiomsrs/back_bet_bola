# Generated by Django 2.0.1 on 2018-03-02 02:08

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20180219_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('seller_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.Seller')),
                ('credit_limit_to_add', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Gerente',
                'verbose_name_plural': 'Gerentes',
                'permissions': (('be_manager', 'Be a manager, permission.'),),
            },
            bases=('user.seller',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterModelOptions(
            name='seller',
            options={'permissions': (('be_seller', 'Be a seller, permission.'), ('set_credit_limit', 'Set the credit limit value')), 'verbose_name': 'Vendedor', 'verbose_name_plural': 'Vendedores'},
        ),
        migrations.AddField(
            model_name='seller',
            name='can_sell_ilimited',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='credit_limit',
            field=models.FloatField(default=0, verbose_name='Limite de Venda'),
        ),
    ]
