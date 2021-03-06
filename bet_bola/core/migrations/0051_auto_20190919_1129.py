# Generated by Django 2.2.4 on 2019-09-19 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20190821_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cotationmodified',
            name='cotation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_modify', to='core.Cotation', verbose_name='Cota Original Modificada'),
        ),
        migrations.AlterField(
            model_name='cotationmodified',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_modify', to='core.Store', verbose_name='Banca'),
        ),
    ]
