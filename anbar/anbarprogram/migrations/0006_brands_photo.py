# Generated by Django 4.2.6 on 2023-10-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0005_remove_brands_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='brand_photos/'),
        ),
    ]
