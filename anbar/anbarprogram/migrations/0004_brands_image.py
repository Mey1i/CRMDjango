# Generated by Django 4.2.6 on 2023-10-23 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0003_suppliers'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='brands/'),
        ),
    ]
