# Generated by Django 3.0.4 on 2020-04-15 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0030_auto_20200415_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='Service_ID',
            field=models.CharField(blank=True, default='', help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>', max_length=10),
        ),
    ]