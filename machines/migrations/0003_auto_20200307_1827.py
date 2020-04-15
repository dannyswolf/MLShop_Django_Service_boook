# Generated by Django 3.0.4 on 2020-03-07 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_auto_20200307_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='machines',
            name='Μοντέλο',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='machines',
            name='Serial',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='machines',
            name='Εναρξη',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]