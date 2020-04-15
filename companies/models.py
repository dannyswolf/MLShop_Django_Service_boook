# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from machines.models import Machines


class Companies(models.Model):

    Εταιρεία = models.CharField(max_length=100, blank=True, null=True)
    Μοντέλο = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Companies'
        verbose_name_plural = 'Εταιρεία - Μοντέλο'
        verbose_name = 'Εταιρεία - Μοντέλο'

    def __str__(self):
        return f'Εταιρεία: {self.Εταιρεία} Μοντέλο:{self.Μοντέλο}'

