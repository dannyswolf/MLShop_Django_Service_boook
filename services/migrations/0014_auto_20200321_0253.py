# Generated by Django 3.0.4 on 2020-03-21 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0013_auto_20200321_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Ημερομηνία',
            field=models.DateField(blank=True, default=' ', null=True),
        ),
    ]