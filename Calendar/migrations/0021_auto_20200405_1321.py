# Generated by Django 3.0.4 on 2020-04-05 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0020_auto_20200403_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='Service_ID',
            field=models.SmallIntegerField(blank=True, help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>', null=True),
        ),
    ]
