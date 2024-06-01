# Generated by Django 4.2.6 on 2023-11-06 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anbarprogram', '0024_planner_accept'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=33)),
                ('surname', models.CharField(max_length=33)),
                ('username', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=24)),
                ('cpassword', models.CharField(max_length=24)),
            ],
        ),
    ]