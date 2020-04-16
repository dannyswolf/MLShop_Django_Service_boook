# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from machines.models import Machines


class CopiersLog(models.Model):
    ID_μηχανήματος = models.ForeignKey(Machines,  models.SET_NULL, blank=True, null=True, db_column='ID_μηχανήματος')

    Μηχάνημα = models.CharField(max_length=200, blank=False, null=False)
    Ημερομηνία = models.CharField(max_length=200, blank=False, null=False)
    Προηγούμενος_Πελάτης = models.CharField(max_length=200, blank=False, null=False)
    Νέος_Πελάτης = models.CharField(max_length=200, blank=False, null=False)
    Σημειώσεις = models.CharField(max_length=200, blank=True, null=True, default='')

    class Meta:
        db_table = 'Copiers_Log'
        verbose_name_plural = 'Μεταφορά - Μηχανημάτων'
        verbose_name = 'Μεταφορά - Μηχανημάτων'

    def __str__(self):
        return f'Μηχάνημα: {self.Μηχάνημα} Προηγούμενος Πελάτης: {self.Προηγούμενος_Πελάτης} ' \
               f'Νέος Πελάτης: {self.Νέος_Πελάτης} Ημερωμηνία: {self.Ημερομηνία}'

