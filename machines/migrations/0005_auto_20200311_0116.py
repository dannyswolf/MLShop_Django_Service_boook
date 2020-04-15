# Generated by Django 3.0.4 on 2020-03-11 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0027_auto_20200310_1106'),
        ('machines', '0004_auto_20200307_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='Πελάτης',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer', to='customers.Customer'),
        ),
    ]
