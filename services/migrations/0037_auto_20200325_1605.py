# Generated by Django 3.0.4 on 2020-03-25 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0036_auto_20200325_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='services',
            options={'ordering': ['-Ημερομηνία']},
        ),
    ]
