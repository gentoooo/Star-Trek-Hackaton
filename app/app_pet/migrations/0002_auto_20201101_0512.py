# Generated by Django 3.1.2 on 2020-10-31 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_pet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petmodel',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='shelter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_pet.shelter'),
        ),
        migrations.AlterField(
            model_name='petmodel',
            name='typevaccine',
            field=models.ManyToManyField(blank=True, null=True, to='app_pet.TypeVaccine'),
        ),
    ]