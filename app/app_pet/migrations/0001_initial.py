# Generated by Django 3.1 on 2020-10-27 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('Telegram', models.CharField(blank=True, max_length=100)),
                ('Vk', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('shelter', models.BooleanField(blank=True, default=False)),
                ('people', models.BooleanField(blank=True, default=True)),
                ('avatar', models.ImageField(blank=True, upload_to='user_photo')),
                ('donate', models.CharField(blank=True, choices=[('s', 'simple'), ('m', 'medium'), ('h', 'hard')], default='s', max_length=1)),
                ('data_start_donat', models.DateField(blank=True, default='0000-00-00')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PetModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_pet', models.CharField(choices=[('d', 'dog'), ('c', 'cat'), ('o', 'other')], default='d', max_length=1)),
                ('sigma', models.BooleanField(default=False)),
                ('found_lost', models.CharField(choices=[('f', 'found'), ('l', 'lost')], default='f', max_length=1)),
                ('data', models.DateTimeField()),
                ('rewards', models.IntegerField()),
                ('image1', models.ImageField(blank=True, upload_to='user_photo')),
                ('image2', models.ImageField(blank=True, upload_to='user_photo')),
                ('image3', models.ImageField(blank=True, upload_to='user_photo')),
                ('image4', models.ImageField(blank=True, upload_to='user_photo')),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
