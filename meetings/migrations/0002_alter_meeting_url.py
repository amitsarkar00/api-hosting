# Generated by Django 3.2.10 on 2022-02-03 08:33

from django.db import migrations, models
import meetings.models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='url',
            field=models.URLField(default=meetings.models.get_default_meeting_url, unique=True),
        ),
    ]
