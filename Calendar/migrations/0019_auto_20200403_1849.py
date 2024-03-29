# Generated by Django 3.0.4 on 2020-04-03 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0037_auto_20200403_1837'),
        ('Calendar', '0018_auto_20200403_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='Copier_ID',
            field=models.ForeignKey(db_column='Copier_ID', help_text='Δεν το αλλάζουμε', on_delete=django.db.models.deletion.PROTECT, to='machines.Machines'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='ΔΤΕ',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='Επείγων',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='Τεχνικός',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
