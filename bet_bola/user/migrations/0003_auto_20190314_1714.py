# Generated by Django 2.1.3 on 2019-03-14 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190314_1714'),
        ('user', '0002_auto_20190313_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='store',
        ),
        migrations.RemoveField(
            model_name='punter',
            name='store',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='store',
        ),
        migrations.AddField(
            model_name='customuser',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Store', verbose_name='Banca'),
            preserve_default=False,
        ),
    ]
