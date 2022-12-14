# Generated by Django 4.1.3 on 2022-12-03 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='child',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=2),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=2),
        ),
    ]
