# Generated by Django 2.1.1 on 2018-10-14 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0007_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='resource.Product_type_three'),
        ),
    ]