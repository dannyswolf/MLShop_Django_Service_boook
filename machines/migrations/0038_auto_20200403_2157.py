# Generated by Django 3.0.4 on 2020-04-03 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0049_auto_20200403_1822'),
        ('machines', '0037_auto_20200403_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='Πελάτης',
            field=models.ForeignKey(db_column='Πελάτη_ID', on_delete=django.db.models.deletion.PROTECT, to='customers.Customer'),
        ),
    ]
