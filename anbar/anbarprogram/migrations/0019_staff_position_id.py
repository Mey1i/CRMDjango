# Generated by Django 4.2.6 on 2023-10-27 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0018_orders_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='position_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='position', to='anbarprogram.positions'),
            preserve_default=False,
        ),
    ]
