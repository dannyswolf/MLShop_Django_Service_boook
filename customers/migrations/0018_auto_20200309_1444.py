# Generated by Django 3.0.4 on 2020-03-09 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0017_auto_20200309_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Κινητό',
            field=models.IntegerField(blank=True, default=69, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Ταχ_Κώδικας',
            field=models.IntegerField(blank=True, default=0, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Τηλέφωνο',
            field=models.IntegerField(blank=True, default=2, null=True, unique=True),
        ),
    ]
