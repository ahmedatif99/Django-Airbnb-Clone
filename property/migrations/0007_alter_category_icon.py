# Generated by Django 4.1.3 on 2022-12-06 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.CharField(max_length=40),
        ),
    ]
