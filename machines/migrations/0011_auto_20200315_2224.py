# Generated by Django 3.0.4 on 2020-03-15 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0034_auto_20200315_1727'),
        ('machines', '0010_auto_20200315_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='Πελάτης',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.Customer'),
        ),
    ]
