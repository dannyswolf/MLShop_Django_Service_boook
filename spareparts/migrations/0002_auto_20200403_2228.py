# Generated by Django 3.0.4 on 2020-04-03 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Calendar', '0020_auto_20200403_2054'),
        ('spareparts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spareparts',
            name='Calendar_ID',
            field=models.ForeignKey(blank=True, db_column='Calendar_ID', help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>', null=True, on_delete=django.db.models.deletion.PROTECT, to='Calendar.Calendar'),
        ),
    ]
