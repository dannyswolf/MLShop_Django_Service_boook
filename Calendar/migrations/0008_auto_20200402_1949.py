# Generated by Django 3.0.4 on 2020-04-02 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0007_auto_20200401_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='Copier_ID',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='Customer_ID',
            field=models.SmallIntegerField(),
        ),
    ]