# Generated by Django 4.2.6 on 2023-11-15 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0042_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
