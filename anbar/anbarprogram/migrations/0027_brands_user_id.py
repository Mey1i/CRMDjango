# Generated by Django 4.2.6 on 2023-11-06 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0026_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='user_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
