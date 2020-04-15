# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from machines.models import Machines


class ReceiverEmails(models.Model):

    Receiver_email = models.CharField(max_length=100, blank=True, null=True, unique=True)

    class Meta:
        db_table = 'Receiver_emails'
        verbose_name_plural = 'Αποδέκτες Emails'
        verbose_name = 'Email Αποδέκτη'

    def __str__(self):
        return f'Email Αποδέκτη: {self.Receiver_email} '

