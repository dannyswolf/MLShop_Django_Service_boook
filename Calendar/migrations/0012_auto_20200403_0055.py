# Generated by Django 3.0.4 on 2020-04-03 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0041_auto_20200330_0820'),
        ('Calendar', '0011_auto_20200403_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='Service_ID',
            field=models.ForeignKey(blank=True, default='0', null=True, on_delete=django.db.models.deletion.PROTECT, to='services.Services'),
        ),
    ]
