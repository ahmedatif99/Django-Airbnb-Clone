# Generated by Django 4.1.3 on 2022-11-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(upload_to='property/'),
        ),
    ]
