# Generated by Django 4.2.6 on 2023-10-27 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0015_products_supplier_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='planner',
            name='staff_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='anbarprogram.staff'),
            preserve_default=False,
        ),
    ]