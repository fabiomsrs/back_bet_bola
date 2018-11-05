# Generated by Django 2.1.3 on 2018-11-05 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0012_auto_20181104_1555'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comission',
            name='four_plus_amount',
        ),
        migrations.RemoveField(
            model_name='comission',
            name='triple_amount',
        ),
        migrations.AddField(
            model_name='comission',
            name='fifth',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Quíntupla'),
        ),
        migrations.AddField(
            model_name='comission',
            name='fourth',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Quádrupla'),
        ),
        migrations.AddField(
            model_name='comission',
            name='sixth',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Sêxtupla'),
        ),
        migrations.AddField(
            model_name='comission',
            name='sixth_more',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Mais de  6'),
        ),
        migrations.AddField(
            model_name='comission',
            name='triple',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Tripla'),
        ),
        migrations.AlterField(
            model_name='comission',
            name='double',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Dupla'),
        ),
        migrations.AlterField(
            model_name='comission',
            name='simple',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10, verbose_name='Simples'),
        ),
    ]