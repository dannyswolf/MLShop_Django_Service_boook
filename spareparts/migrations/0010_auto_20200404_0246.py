# Generated by Django 3.0.4 on 2020-04-04 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0038_auto_20200403_2157'),
        ('spareparts', '0009_auto_20200404_0201'),
    ]

    operations = [
        migrations.AddField(
            model_name='spareparts',
            name='Serial',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='spareparts',
            name='Εταιρεία',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='ΜΗΧΑΝΗΜΑ',
            field=models.ForeignObject(db_column='ΜΗΧΑΝΗΜΑ', from_fields=('ΜΗΧΑΝΗΜΑ', 'Serial'), on_delete=django.db.models.deletion.PROTECT, to='machines.Machines', to_fields=('Εταιρεία', 'Serial')),
        ),
    ]
