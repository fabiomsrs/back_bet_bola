# Generated by Django 2.2.3 on 2019-07-17 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_auto_20190717_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail'),
            preserve_default=False,
        ),
    ]
