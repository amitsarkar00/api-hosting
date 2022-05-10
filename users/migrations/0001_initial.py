# Generated by Django 3.2.10 on 2022-01-14 21:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('title', models.CharField(default=None, max_length=5, null=True)),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15, null=True, unique=True)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('token', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('role', models.CharField(default='ROLE_USER', max_length=10)),
                ('email_verified', models.BooleanField(default=False)),
                ('phone_number_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('extra_fields', models.TextField(null=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
