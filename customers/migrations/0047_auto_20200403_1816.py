# Generated by Django 3.0.4 on 2020-04-03 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0046_auto_20200403_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Κινητό',
            field=models.CharField(blank=True, max_length=15, null=True, unique=False),
        ),
    ]
