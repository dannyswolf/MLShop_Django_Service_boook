# Generated by Django 3.0.4 on 2020-03-20 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20200320_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='Ημερομηνία',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
