# Generated by Django 3.0.4 on 2020-03-10 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0025_auto_20200310_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Κινητό',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]