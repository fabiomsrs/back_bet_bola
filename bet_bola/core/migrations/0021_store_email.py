# Generated by Django 2.1.7 on 2019-03-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20190326_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]