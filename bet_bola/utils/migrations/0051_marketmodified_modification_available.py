# Generated by Django 2.2.4 on 2019-09-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utils', '0050_auto_20190829_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketmodified',
            name='modification_available',
            field=models.BooleanField(default=False),
        ),
    ]
