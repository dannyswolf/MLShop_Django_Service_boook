# Generated by Django 3.0.4 on 2020-03-09 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0013_auto_20200306_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Τηλέφωνο',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]