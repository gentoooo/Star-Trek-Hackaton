# Generated by Django 3.1.2 on 2020-11-01 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet', '0003_auto_20201101_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petmodel',
            name='image',
        ),
    ]
