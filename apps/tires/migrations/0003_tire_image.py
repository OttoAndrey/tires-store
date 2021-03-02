# Generated by Django 3.1.6 on 2021-02-17 10:37

import apps.tires.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tires', '0002_remove_tire_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='tire',
            name='image',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to=apps.tires.models.upload_tire_image_to, verbose_name='Tire image'),
        ),
    ]
