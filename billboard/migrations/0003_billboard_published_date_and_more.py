# Generated by Django 4.2.16 on 2024-11-09 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0002_alter_billboard_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='billboard',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='billboard',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 9, 14, 53, 33, 176415, tzinfo=datetime.timezone.utc)),
        ),
    ]