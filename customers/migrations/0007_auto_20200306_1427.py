# Generated by Django 3.0.4 on 2020-03-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20200306_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Διεύθυνση',
            field=models.CharField(blank=True, choices=[('Φ', 'Φλώρινα'), ('Α', 'Αμυνταιο'), ('Μ', 'Μελιτη')], max_length=200, null=True),
        ),
    ]
