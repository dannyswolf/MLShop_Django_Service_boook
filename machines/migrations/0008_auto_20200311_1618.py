# Generated by Django 3.0.4 on 2020-03-11 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0031_auto_20200311_1618'),
        ('machines', '0007_auto_20200311_1611'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='machines',
            options={},
        ),
        migrations.AlterField(
            model_name='machines',
            name='Πελάτης',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.Customer', verbose_name='pelatis'),
        ),
    ]
