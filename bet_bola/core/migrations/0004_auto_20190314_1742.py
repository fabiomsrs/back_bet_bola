# Generated by Django 2.1.3 on 2019-03-14 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20190314_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='store',
            name='username',
        ),
        migrations.AddField(
            model_name='store',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_store', to=settings.AUTH_USER_MODEL, verbose_name='Dono'),
        ),
    ]
