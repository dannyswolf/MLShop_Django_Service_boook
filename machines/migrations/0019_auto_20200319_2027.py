# Generated by Django 3.0.4 on 2020-03-19 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0018_auto_20200319_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='Εναρξη',
            field=models.DateField(blank=True, null=True),
        ),
    ]
