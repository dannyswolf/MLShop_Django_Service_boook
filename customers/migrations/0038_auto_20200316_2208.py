# Generated by Django 3.0.4 on 2020-03-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0037_auto_20200316_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Σημειώσεις',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
