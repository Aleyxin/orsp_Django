# Generated by Django 2.1.1 on 2018-10-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_adminmsg'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='integral',
            field=models.IntegerField(default=1),
        ),
    ]
