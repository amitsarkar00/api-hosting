# Generated by Django 3.2.10 on 2022-02-01 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0002_auto_20220129_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_login', models.BooleanField(default=False)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.company')),
                ('created_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='admin_created', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]