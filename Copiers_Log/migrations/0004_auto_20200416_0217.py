# Generated by Django 3.0.4 on 2020-04-15 23:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0041_auto_20200415_0421'),
        ('Copiers_Log', '0003_auto_20200416_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='copierslog',
            name='ID_μηχανήματος',
            field=models.ForeignKey(blank=True, db_column='ID_μηχανήματος', null=True, on_delete=django.db.models.deletion.SET_NULL, to='machines.Machines'),
        ),
    ]
