# Generated by Django 4.1.3 on 2022-12-04 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_propertybook_child_alter_propertybook_guest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='child',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
