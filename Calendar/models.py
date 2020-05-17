# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from machines.models import Machines
from datetime import datetime


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/Service_ID/<filename>
    return '{0}/{1}'.format(instance.Service_ID, filename)



class Calendar(models.Model):

    # customer = list(Customer.objects.filter(Κατάσταση=True))
    Ημερομηνία = models.CharField(help_text='Ημερομηνία', max_length=10)
    Πελάτης = models.CharField(max_length=100, unique=False, blank=False, null=False)
    Μηχάνημα = models.CharField(max_length=100, unique=False, blank=False, null=False)
    Σκοπός = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    Ενέργειες = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    Τεχνικός = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    Ημ_Ολοκλ = models.CharField(help_text='Ημερομηνία ολοκλήρωσης', null=False, blank=True, max_length=10, default="")
    Επείγων = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    Τηλέφωνο = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")
    Σημειώσεις = models.TextField(max_length=5000, unique=False, blank=True, null=False, default="")

    Copier_ID = models.ForeignKey(Machines, blank=False, null=False, on_delete=models.PROTECT, db_column='Copier_ID',
                                  help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')

    ΔΤΕ = models.CharField(max_length=100, unique=False, blank=True, null=False, default="")

    Service_ID = models.CharField(null=False, blank=True, default="", max_length=10,
                                  help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')

    Μετρητής = models.CharField(max_length=11, unique=False, blank=True, null=False, default="")
    Επ_Service = models.CharField(max_length=11, unique=False, blank=True, null=False, default="")

    Customer_ID = models.SmallIntegerField(blank=False, null=False,
                                           help_text='<font color="white"><b>Δεν το αλλάζουμε</b></font>')

    Price = models.CharField(max_length=100, blank=True, null=True, )

    Κατάσταση = models.BooleanField(default=True)
    file = models.FileField(upload_to=user_directory_path, default="", )

    class Meta:
        db_table = 'Calendar'
        ordering = ['Ημερομηνία']
        verbose_name_plural = 'Ημερολόγιο'
        verbose_name = 'Εργασίες'

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('Calendar:list_calendar', kwargs={'Copier_ID': self.pk})

    def __str__(self):
        return f'{self.Ημερομηνία} {self.Πελάτης}  {self.Μηχάνημα}'
