# Generated by Django 4.2.6 on 2023-11-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0032_suppliers_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
