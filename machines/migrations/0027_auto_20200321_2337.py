# Generated by Django 3.0.4 on 2020-03-21 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0026_auto_20200321_2334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machines',
            old_name='Πελάτη_ID',
            new_name='Πελάτης',
        ),
    ]
