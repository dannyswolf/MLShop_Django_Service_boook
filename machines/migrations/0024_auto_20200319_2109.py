# Generated by Django 3.0.4 on 2020-03-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0023_auto_20200319_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='Εναρξη',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
