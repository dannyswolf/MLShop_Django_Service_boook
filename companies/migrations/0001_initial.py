# Generated by Django 3.0.4 on 2020-04-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Εταιρεία', models.CharField(blank=True, max_length=100, null=True)),
                ('Μοντέλο', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Εταιρεία - Μοντέλο',
                'verbose_name_plural': 'Εταιρεία - Μοντέλο',
                'db_table': 'Companies',
            },
        ),
    ]
