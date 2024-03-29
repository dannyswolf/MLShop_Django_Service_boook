# Generated by Django 3.0.4 on 2020-04-15 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CopiersLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_μηχανήματος', models.SmallIntegerField(help_text='ID_μηχανήματος')),
                ('Μηχάνημα', models.CharField(max_length=200)),
                ('Ημερωμηνία', models.CharField(max_length=200)),
                ('Προηγούμενος_Πελάτης', models.CharField(max_length=200)),
                ('Νέος_Πελάτης', models.CharField(max_length=200)),
                ('Σημειώσεις', models.CharField(blank=True, default='', max_length=200)),
            ],
            options={
                'verbose_name': 'Μεταφορά - Μηχανημάτων',
                'verbose_name_plural': 'Μεταφορά - Μηχανημάτων',
                'db_table': 'Copiers_Log',
            },
        ),
    ]
