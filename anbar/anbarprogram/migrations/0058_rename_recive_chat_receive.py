# Generated by Django 4.2.6 on 2023-11-29 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0057_rename_tarix_chat_date_rename_qebul_chat_recive_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='recive',
            new_name='receive',
        ),
    ]
