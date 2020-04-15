# -*- coding: utf-8 -*-
from django.db import models
from django.urls import reverse
from machines.models import Machines


class SenderEmails(models.Model):

    sender_email = models.CharField(max_length=100, blank=True, null=True, unique=True)
    password = models.CharField(max_length=100, blank=True, null=True, unique=False)
    smtp_server = models.CharField(max_length=100, blank=True, null=True, unique=False)
    port = models.SmallIntegerField(blank=True, null=True, unique=False)

    class Meta:
        db_table = 'Sender_emails'
        verbose_name_plural = 'Αποστολής Emails'
        verbose_name = 'Email Αποστολέα'

    def __str__(self):
        return f'Email Αποστολέα: {self.sender_email} '

