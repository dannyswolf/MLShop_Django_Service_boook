# Generated by Django 3.0.4 on 2020-03-05 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='Νame',
        ),
    ]
