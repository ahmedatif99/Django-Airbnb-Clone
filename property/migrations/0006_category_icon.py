# Generated by Django 4.1.3 on 2022-12-05 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_alter_propertybook_child_alter_propertybook_guest'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
