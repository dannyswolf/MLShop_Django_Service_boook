# Generated by Django 3.0.4 on 2020-03-10 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0022_auto_20200310_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Κινητό',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]