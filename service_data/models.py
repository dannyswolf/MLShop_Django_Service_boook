# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from machines.models import Machines


class ServiceData(models.Model):
    # customer = list(Customer.objects.filter(Κατάσταση=True))
    Σκοπός = models.CharField(help_text='Περιγραφή προβλήματος', max_length=100, blank=True, null=True)
    Ενέργειες = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Service_data'
        verbose_name_plural = 'Σκοπός - Ενέργειες'
        verbose_name = 'Σκοπός - Ενέργειες'

    def __str__(self):
        return f'Σκοπός: {self.Σκοπός} Ενέργειες:{self.Ενέργειες}'

