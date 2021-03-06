# Generated by Django 2.1.7 on 2019-03-18 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190318_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('period_type', models.IntegerField(choices=[(10, 'Primeiro Tempo'), (20, 'Segundo Tempo'), (30, 'Primeiro Tempo (Prorrogacao)'), (35, 'Segundo Tempo (Prorrogacao)'), (50, 'Penaltis'), (100, 'Termino'), (101, 'Termino (Prorrogacao)'), (102, 'Termino (Penaltis')])),
                ('is_fineshed', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('home_score', models.IntegerField(default=0)),
                ('away_score', models.IntegerField(default=0)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='periods', to='core.Game')),
            ],
        ),
    ]
