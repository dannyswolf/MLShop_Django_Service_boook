# Generated by Django 3.0.4 on 2020-04-04 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0038_auto_20200403_2157'),
        ('spareparts', '0008_auto_20200403_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spareparts',
            name='ΜΗΧΑΝΗΜΑ',
            field=models.ForeignKey(db_column='ΜΗΧΑΝΗΜΑ', on_delete=django.db.models.deletion.PROTECT, to='machines.Machines', to_field='Serial'),
        ),
    ]