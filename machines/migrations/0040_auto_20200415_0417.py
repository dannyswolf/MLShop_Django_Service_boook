# Generated by Django 3.0.4 on 2020-04-15 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0039_auto_20200415_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machines',
            name='Εναρξη',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]