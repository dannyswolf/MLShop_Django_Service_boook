# Generated by Django 3.0.4 on 2020-04-15 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Copiers_Log', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copierslog',
            name='Σημειώσεις',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
