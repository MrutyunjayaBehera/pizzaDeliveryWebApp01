# Generated by Django 3.1.3 on 2021-04-15 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaApp', '0004_oredermodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrederModel',
            new_name='OrderModel',
        ),
    ]