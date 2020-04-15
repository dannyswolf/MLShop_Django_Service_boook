from django.db import models
from django.urls import reverse

"""

I got a field with attribute unique, which was not unique [eg 2-time same value]
Error -->>  django.db.utils.IntegrityError: UNIQUE constraint failed:
python3 manage.py migrate --fake

then

python3 manage.py makemigrations

python3 manage.py migrate

"""


# Create your models here.
class Customer(models.Model):
    class Meta:
        ordering = ['Επωνυμία_Επιχείρησης']
        db_table = 'Πελάτες'
        verbose_name_plural = 'Πελάτες'
        verbose_name = 'Πελάτες'

    Περιοχές = models.TextChoices('Περιοχές', 'Φλώρινα Αμύνταιο Μελίτη')
    Επωνυμία_Επιχείρησης = models.CharField(max_length=200, blank=False, null=False, unique=True)
    Ονοματεπώνυμο = models.CharField(max_length=200, blank=True, null=True, default="")
    Διεύθυνση = models.CharField(max_length=200, blank=True, null=True, default="")
    Πόλη = models.CharField(max_length=100, blank=True, null=True, choices=Περιοχές.choices, default="Φλώρινα")
    Ταχ_Κώδικας = models.CharField(blank=True, null=True, max_length=200)
    Περιοχή = models.CharField(max_length=200, blank=True, null=True, choices=Περιοχές.choices, default="Φλώρινα")
    Τηλέφωνο = models.CharField(blank=True, null=True, max_length=15, unique=False)
    Κινητό = models.CharField(blank=True, null=True, max_length=15, unique=False)
    Φαξ = models.CharField(blank=True, null=True, max_length=13)
    E_mail = models.EmailField(max_length=50, blank=True, null=True)
    Σελίδες_πακέτου = models.CharField(max_length=10, blank=True, null=True)
    Κόστος_πακέτου = models.CharField(max_length=20, blank=True, null=True)
    Σημειώσεις = models.TextField(max_length=500, blank=True, null=True)
    Κατάσταση = models.BooleanField(default=True, help_text="<strong>Ενεργός πελάτης</strong>")

    def __str__(self):
        return self.Επωνυμία_Επιχείρησης

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('customers:list_customers', kwargs={'customer_id': self.pk})
