# Generated by Django 3.0.4 on 2020-04-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Σκοπός', models.CharField(blank=True, help_text='Περιγραφή προβλήματος', max_length=100, null=True)),
                ('Ενέργειες', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Σκοπός - Ενέργειες',
                'verbose_name_plural': 'Σκοπός - Ενέργειες',
                'db_table': 'Service_data',
            },
        ),
    ]