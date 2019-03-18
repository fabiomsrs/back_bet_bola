# Generated by Django 2.1.3 on 2019-03-18 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190315_1827'),
        ('user', '0006_auto_20190315_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='normaluser',
            name='my_store',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Store', verbose_name='Banca'),
            preserve_default=False,
        ),
    ]
