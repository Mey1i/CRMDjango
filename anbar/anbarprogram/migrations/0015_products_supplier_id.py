# Generated by Django 4.2.6 on 2023-10-26 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0014_orders_client_id_alter_products_brand_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='supplier_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='supplier', to='anbarprogram.suppliers'),
            preserve_default=False,
        ),
    ]
