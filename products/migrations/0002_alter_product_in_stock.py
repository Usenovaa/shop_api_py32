# Generated by Django 4.2.10 on 2024-02-20 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(default='True'),
        ),
    ]
