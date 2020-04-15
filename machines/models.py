from django.db import models
from customers.models import Customer
from django.urls import reverse

# Create your models here.


class Machines(models.Model):

    Εταιρεία = models.CharField(max_length=100, blank=False, null=False)
    Serial = models.CharField(max_length=30, blank=False, null=False, unique=True)
    # Εναρξη = models.DateField(auto_now=False, auto_created=False, blank=True, null=True)
    Εναρξη = models.CharField(max_length=200, blank=True, default="")
    # Μετρητής_έναρξης = models.PositiveIntegerField(blank=True, null=True)
    Μετρητής_έναρξης = models.CharField(max_length=200, blank=True, default="")
    Πελάτης = models.ForeignKey(Customer, on_delete=models.PROTECT, null=False, blank=False, db_column='Πελάτη_ID')
    Σημειώσεις = models.TextField(max_length=500, blank=True, null=True)
    Κατάσταση = models.BooleanField(default=True, help_text='<font color="red"><b>Ενεργό αν δεν έχει αποσυρθεί το μηχάνημα</b></font>')

    class Meta:
        db_table = 'Φωτοτυπικά'
        ordering = ['Εταιρεία']
        verbose_name_plural = 'Φωτοτυπικά'
        verbose_name = 'Μηχανήματα'

    def __str__(self):
        return f'{self.pk} {self.Εταιρεία} Serial:{self.Serial}'

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('machines:edit_machine', kwargs={'machine_id': self.pk})
