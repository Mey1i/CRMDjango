# Generated by Django 4.2.6 on 2023-11-06 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0028_clients_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='departments',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
