# Generated by Django 3.0.4 on 2020-04-05 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiverEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Receiver_email', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Email Αποδέκτη',
                'verbose_name_plural': 'Αποδέκτες Emails',
                'db_table': 'Receiver_emails',
            },
        ),
    ]
