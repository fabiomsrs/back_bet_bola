# Generated by Django 2.2.2 on 2019-06-21 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20190517_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotationcopy',
            name='store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='my_cotation_copies', to='core.Store', verbose_name='Banca'),
            preserve_default=False,
        ),
    ]
