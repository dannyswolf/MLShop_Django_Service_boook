# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from machines.models import Machines
from Calendar.models import Calendar
from customers.models import Customer
from services.models import Services
from django.core import serializers

class SpareParts(models.Model):
    PARTS_NR = models.CharField(max_length=100, blank=True, null=True)
    ΠΕΡΙΓΡΑΦΗ = models.CharField(max_length=500, blank=True, null=True)
    ΚΩΔΙΚΟΣ = models.CharField(max_length=100, blank=True, null=True)
    ΤΕΜΑΧΙΑ = models.CharField(max_length=100, blank=True, null=True)
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(max_length=1000, blank=True, null=True, default=" ")

    ΜΗΧΑΝΗΜΑ = models.CharField(max_length=200, blank=False, null=False, default="",
                                help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')
    # to_fields=['Εταιρεία', 'Serial'],
    # Εταιρεία = models.CharField(max_length=100, blank=True, null=True, default="")
    #                            #
    # Serial = models.CharField(max_length=100, blank=True, null=True, default="")
    #
    # ΜΗΧΑΝΗΜΑ = models.ForeignObject(Machines, from_fields=['ΜΗΧΑΝΗΜΑ', 'Serial'], to_fields=['Εταιρεία', 'Serial'],
    #                                 blank=False, null=False, on_delete=models.PROTECT)
    #                              db_column='ΜΗΧΑΝΗΜΑ',
    #                              help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')

    Service_ID = models.ForeignKey(Services, blank=False, null=False, on_delete=models.PROTECT,
                                    db_column='Service_ID',
                                    help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')

    Customer_ID = models.ForeignKey(Customer, blank=False, null=False, on_delete=models.PROTECT,
                                    db_column='Customer_ID',
                                    help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')

    Calendar_ID = models.CharField(null=True, blank=True, db_column='Calendar_ID', max_length=10,
                                           help_text='<font color="red"><b>Δεν το αλλάζουμε</b></font>')

    class Meta:
        db_table = 'Ανταλλακτικά'
        verbose_name_plural = 'Ανταλλακτικά'
        verbose_name = 'Ανταλλακτικό'

    def __str__(self):
        return f'{self.ΠΕΡΙΓΡΑΦΗ[:30]} ΚΩΔΙΚΟΣ:{self.ΚΩΔΙΚΟΣ} '

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('spareparts:edit_sparepart', kwargs={'spareparts_id': self.pk})


    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('spareparts:delete_sparepart', kwargs={'spareparts_id': self.pk})

    def serialize(self):
        return {

            'id': self.id,
            'PARTS_NR': self.PARTS_NR,
            'ΠΕΡΙΓΡΑΦΗ': self.ΠΕΡΙΓΡΑΦΗ,
            'ΚΩΔΙΚΟΣ': self.ΚΩΔΙΚΟΣ,
            'ΤΕΜΑΧΙΑ': self.ΤΕΜΑΧΙΑ,
            'ΠΑΡΑΤΗΡΗΣΗΣ': self.ΠΑΡΑΤΗΡΗΣΗΣ,
            'ΜΗΧΑΝΗΜΑ': self.ΜΗΧΑΝΗΜΑ,
            'Service_ID': self.Service_ID,
            'Customer_ID': self.Customer_ID,
            'Calendar_ID': self.Calendar_ID

        }
        