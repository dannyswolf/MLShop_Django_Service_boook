# Generated by Django 3.0.4 on 2020-04-03 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0045_auto_20200403_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Κατάσταση',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
