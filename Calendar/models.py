# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from customers.models import Customer
from machines.models import Machines
from services.models import Services


class Calendar(models.Model):
    # customer = list(Customer.objects.filter(Κατάσταση=True))
    Ημερομηνία = models.CharField(help_text='Ημερομηνία', max_length=10)
    Πελάτης = models.CharField(max_length=100, unique=False, blank=False, null=False,)
    Μηχάνημα = models.CharField(max_length=100, unique=False, blank=False, null=False)
    Σκοπός = models.CharField(max_length=100, unique=False, blank=True, null=True)
    Ενέργειες = models.CharField(max_length=100, unique=False, blank=True, null=True)
    Τεχνικός = models.CharField(max_length=100, unique=False, blank=True, null=True, default="")
    Ημ_Ολοκλ = models.CharField(help_text='Ημερομηνία ολοκλήρωσης', null=True, blank=True, max_length=10)
    Επείγων = models.CharField(max_length=100, unique=False, blank=True, null=True, default="")
    Τηλέφωνο = models.CharField(max_length=100, unique=False, blank=True, null=True)
    Σημειώσεις = models.CharField(max_length=5000, unique=False, blank=True, null=True)
    Copier_ID = models.ForeignKey(Machines, blank=False, null=False, on_delete=models.PROTECT, db_column='Copier_ID',
                                  help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')
    ΔΤΕ = models.CharField(max_length=100, unique=False, blank=True, null=True, default="")
    Service_ID = models.SmallIntegerField(null=True, blank=True, help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')
    Μετρητής = models.CharField(max_length=11, unique=False, blank=True, null=True)
    Επ_Service = models.CharField(max_length=11, unique=False, blank=True, null=True)
    Customer_ID = models.SmallIntegerField(blank=False, null=False, help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')
    Price = models.CharField(max_length=100, unique=False, blank=True, null=True)
    Κατάσταση = models.BooleanField(default=True, help_text='<font color="red"><b>Ενεργό αν δεν έχει τελειώσει η εργασία</b></font>')

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
