# Generated by Django 2.1.3 on 2019-03-15 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_store_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='location',
        ),
    ]
