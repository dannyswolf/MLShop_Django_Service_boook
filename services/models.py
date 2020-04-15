from django.db import models
from django.urls import reverse
from machines.models import Machines
from datetime import datetime
"""

I got a field with attribute unique, which was not unique [eg 2-time same value]
Error -->>  django.db.utils.IntegrityError: UNIQUE constraint failed:
python3 manage.py migrate --fake

then

python3 manage.py makemigrations

python3 manage.py migrate

"""


# Create your models here.
class Services(models.Model):

    class Meta:
        # dates.sort(key=lambda date: datetime.strptime(date, '%d %b %Y'))
        # data_from_calendar = c.fetchall()
        # sorted_data_from_calendar = sorted(data_from_calendar, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))
        # sorted(unsorted_results, key= lambda t: t.thing_date())
        #sorted_data_from_calendar = sorted(data_from_calendar, key=lambda x: datetime.strptime(x[1], "%d/%m/%Y"))
        ordering = ['-ΔΤΕ']
        db_table = 'Service'
        verbose_name_plural = 'Συντήρηση'
        verbose_name = 'Συντήρηση'

    Ημερομηνία = models.CharField(max_length=10, blank=True, null=True)
    Σκοπός_Επίσκεψης = models.CharField(max_length=300, blank=False, null=False)
    Ενέργειες = models.CharField(max_length=200, blank=True, null=True, default="")
    Τεχνικός = models.CharField(max_length=200, blank=True, null=True, default="")
    Σημειώσεις = models.TextField(max_length=500, blank=True, null=True)
    Μετρητής = models.CharField(max_length=11, unique=False, blank=True, null=True)
    Επ_Service = models.CharField(max_length=11, unique=False, blank=True, null=True)
    Copier_ID = models.ForeignKey(Machines, on_delete=models.PROTECT, blank=False, null=False, db_column='Copier_ID',)
    ΔΤΕ = models.CharField(blank=True, null=True, max_length=20)
    Price = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return f'{self.Copier_ID} Ημερομηνία: {self.Ημερομηνία}  Σκοπός Επίσκεψης: {self.Σκοπός_Επίσκεψης} Τεχνικός: {self.Τεχνικός} '

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('service:detail', kwargs={'Copier_ID': self.pk})


