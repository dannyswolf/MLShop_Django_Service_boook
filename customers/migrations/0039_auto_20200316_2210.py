# Generated by Django 3.0.4 on 2020-03-16 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0038_auto_20200316_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Τηλέφωνο',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
