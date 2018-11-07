# Generated by Django 2.1.1 on 2018-10-13 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_type_three',
            name='two_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resource.Product_type_two'),
        ),
        migrations.AddField(
            model_name='product_type_two',
            name='two_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resource.Product_type_one'),
        ),
    ]