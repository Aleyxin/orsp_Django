# Generated by Django 2.1.1 on 2018-10-13 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.IntegerField()),
                ('password', models.CharField(max_length=100)),
                ('regist_time', models.DateTimeField(auto_now_add=True)),
                ('one', models.CharField(max_length=50)),
            ],
        ),
    ]