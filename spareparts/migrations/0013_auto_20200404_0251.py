# Generated by Django 3.0.4 on 2020-04-04 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0012_auto_20200404_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spareparts',
            name='Serial',
        ),
        migrations.RemoveField(
            model_name='spareparts',
            name='Εταιρεία',
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='ΜΗΧΑΝΗΜΑ',
            field=models.CharField(default='', help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>', max_length=100),
        ),
    ]
