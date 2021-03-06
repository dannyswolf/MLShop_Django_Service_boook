# Generated by Django 3.0.4 on 2020-04-11 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0045_auto_20200403_2206'),
        ('Calendar', '0022_auto_20200405_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='Customer_ID',
            field=models.SmallIntegerField(help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='Service_ID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.Services'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='Κατάσταση',
            field=models.BooleanField(default=True, help_text='<font color="red"><b>Ενεργό αν δεν έχει τελειώσει η εργασία</b></font>'),
        ),
    ]
