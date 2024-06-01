# Generated by Django 4.2.6 on 2023-10-27 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0017_positions_department_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='product_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='anbarprogram.products'),
            preserve_default=False,
        ),
    ]
