# Generated by Django 3.0.4 on 2020-03-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0025_auto_20200322_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Ημερομηνία',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
