# Generated by Django 3.0.4 on 2020-03-21 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0014_auto_20200321_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Ημερομηνία',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
