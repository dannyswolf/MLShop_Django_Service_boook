# Generated by Django 3.0.4 on 2020-03-19 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20200319_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Ημερομηνία',
            field=models.DateField(blank=True, null=True),
        ),
    ]
