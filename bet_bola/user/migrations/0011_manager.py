# Generated by Django 2.0.1 on 2018-03-10 01:21

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20180310_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credit_limit_to_add', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Gerente',
                'verbose_name_plural': 'Gerentes',
                'permissions': (('be_manager', 'Be a manager, permission.'),),
            },
            bases=('user.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]