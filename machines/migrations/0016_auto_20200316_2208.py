# Generated by Django 3.0.4 on 2020-03-16 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0015_auto_20200316_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='Σημειώσεις',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
