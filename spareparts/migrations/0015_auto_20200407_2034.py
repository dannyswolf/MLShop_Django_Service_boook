# Generated by Django 3.0.4 on 2020-04-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0014_auto_20200405_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spareparts',
            name='Calendar_ID',
            field=models.SmallIntegerField(blank=True, db_column='Calendar_ID', default='', help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>', null=True),
        ),
        migrations.AlterField(
            model_name='spareparts',
            name='ΠΑΡΑΤΗΡΗΣΗΣ',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]