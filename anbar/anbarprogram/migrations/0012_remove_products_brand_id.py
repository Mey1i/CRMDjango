# Generated by Django 4.2.6 on 2023-10-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0011_products_brand_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='brand_id',
        ),
    ]
