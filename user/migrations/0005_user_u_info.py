# Generated by Django 2.1.1 on 2018-10-13 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181013_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='u_info',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user.Info'),
        ),
    ]
