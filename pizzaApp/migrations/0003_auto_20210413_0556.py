# Generated by Django 3.1.3 on 2021-04-13 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaApp', '0002_customermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='phoneno',
            field=models.IntegerField(),
        ),
    ]
