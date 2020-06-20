# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.shortcuts import reverse
from django_project.settings import SPARE_PARTS_ROOT, SPARE_PARTS_URL
import os

class A_ΟΡΟΦΟΣ(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ΕΤΑΙΡΙΑ = models.CharField(db_column='ΕΤΑΙΡΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=20)  # Field name made lowercase.
    TEMAXIA = models.IntegerField(db_column='TEMAXIA', blank=True, null=True)  # Field name made lowercase.
    ΤΙΜΗ = models.CharField(db_column='ΤΙΜΗ', blank=True, null=True, max_length=10)  # Field name made lowercase.
    ΣΥΝΟΛΟ = models.CharField(db_column='ΣΥΝΟΛΟ', blank=True, null=True, max_length=10)  # Field name made lowercase.
    ΣΕΛΙΔΕΣ = models.CharField(db_column='ΣΕΛΙΔΕΣ', blank=True, null=True, max_length=20)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'A_ΟΡΟΦΟΣ'

    def __str__(self):
        return f"{self.ΕΤΑΙΡΙΑ} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_A_ΟΡΟΦΟΣ', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:A_ΟΡΟΦΟΣ_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.id}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())

class BROTHER(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BROTHER'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_brother', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:brother_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.ID}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class CANON(models.Model):
    ID = models.AutoField(db_column='id', primary_key=True, blank=True, null=False)
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CANON'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_canon', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:canon_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.ID}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class EPSON(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EPSON'

    def __str__(self):
        return f"PARTS_NR :{self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_epson', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:epson_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class Images(models.Model):
    ID = models.TextField(db_column='ID', blank=True, null=False)  # Field name made lowercase.
    Filename = models.TextField(db_column='Filename', blank=True, null=True)  # Field name made lowercase.
    Type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    File_size = models.TextField(db_column='File_size', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    File = models.BinaryField(db_column='File', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.TextField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Images'


class KONICA(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KONICA'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_konica', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:konica_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.ID}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class KYOCERA(models.Model):
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KYOCERA'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_kyocera', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:kyocera_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())

class LEXMARK(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LEXMARK'

    def __str__(self):
        return f"PARTS_NR :{self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_lexmark', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:lexmark_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class OKI(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OKI'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_oki', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:oki_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class RICOH(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RICOH'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_ricoh', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:ricoh_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class SAMSUNG(models.Model):
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)   # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SAMSUNG'

    def __str__(self):
        return f"PARTS_NR: {self.PARTS_NR} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_samsung', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:samsung_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class SHARP(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    PARTS_NR = models.CharField(db_column='PARTS_NR', blank=True, null=True, max_length=50)  # Field name made lowercase
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SHARP'

    def __str__(self):
        return f'{self.PARTS_NR}   ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ}    Κωδικός: {self.ΚΩΔΙΚΟΣ}'

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_sharp', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:sharp_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class ΜΕΛΑΝΑΚΙΑ(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ΕΤΑΙΡΕΙΑ = models.CharField(db_column='ΕΤΑΙΡΕΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΟΙΟΤΗΤΑ = models.CharField(db_column='ΠΟΙΟΤΗΤΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΑΝΑΛΩΣΙΜΟ = models.CharField(db_column='ΑΝΑΛΩΣΙΜΟ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.IntegerField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True)  # Field name made lowercase.
    ΤΙΜΗ = models.CharField(db_column='ΤΙΜΗ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΣΥΝΟΛΟ = models.CharField(db_column='ΣΥΝΟΛΟ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΣΕΛΙΔΕΣ = models.CharField(db_column='ΣΕΛΙΔΕΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΛΑΤΕΣ = models.TextField(db_column='ΠΕΛΑΤΕΣ', blank=True, null=True)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ΜΕΛΑΝΑΚΙΑ'

    def __str__(self):
        return f"{self.ΕΤΑΙΡΕΙΑ} ΠΕΡΙΓΡΑΦΗ: {self.ΠΟΙΟΤΗΤΑ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_melanakia', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:melanakia_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class ΜΕΛΑΝΟΤΑΙΝΙΕΣ(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ΕΤΑΙΡΙΑ = models.CharField(db_column='ΕΤΑΙΡΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΟΙΟΤΗΤΑ = models.CharField(db_column='ΠΟΙΟΤΗΤΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΑΝΑΛΩΣΙΜΟ = models.CharField(db_column='ΑΝΑΛΩΣΙΜΟ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΙΜΗ = models.CharField(db_column='ΤΙΜΗ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΣΥΝΟΛΟ = models.CharField(db_column='ΣΥΝΟΛΟ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΚΩΔΙΚΟΙ = models.CharField(db_column='ΚΩΔΙΚΟΙ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΛΑΤΕΣ = models.TextField(db_column='ΠΕΛΑΤΕΣ', blank=True, null=True)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ΜΕΛΑΝΟΤΑΙΝΙΕΣ'

    def __str__(self):
        return f"ΕΤΑΙΡΕΙΑ:{self.ΕΤΑΙΡΙΑ} ΠΟΙΟΤΗΤΑ: {self.ΠΟΙΟΤΗΤΑ} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_melanotainies', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:melanotainies_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class ΤΟΝΕΡ(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ΕΤΑΙΡΕΙΑ = models.CharField(db_column='ΕΤΑΙΡΕΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΟΙΟΤΗΤΑ = models.CharField(db_column='ΠΟΙΟΤΗΤΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΑΝΑΛΩΣΙΜΟ = models.CharField(db_column='ΑΝΑΛΩΣΙΜΟ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΙΜΗ = models.CharField(db_column='ΤΙΜΗ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΣΥΝΟΛΟ = models.CharField(db_column='ΣΥΝΟΛΟ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΣΕΛΙΔΕΣ = models.CharField(db_column='ΣΕΛΙΔΕΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΛΑΤΕΣ = models.CharField(db_column='ΠΕΛΑΤΕΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ΤΟΝΕΡ'

    def __str__(self):
        return f"ΕΤΑΙΡΕΙΑ:{self.ΕΤΑΙΡΕΙΑ} ΠΕΡΙΓΡΑΦΗ: {self.ΠΟΙΟΤΗΤΑ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_toner', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        return reverse('warehouse:toner_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.ID}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class ΦΩΤΟΤΥΠΙΚΑ(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ΕΤΑΙΡΕΙΑ = models.CharField(db_column='ΕΤΑΙΡΕΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΟΙΟΤΗΤΑ = models.CharField(db_column='ΠΟΙΟΤΗΤΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΑΝΑΛΩΣΙΜΟ = models.CharField(db_column='ΑΝΑΛΩΣΙΜΟ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΕΜΑΧΙΑ = models.CharField(db_column='ΤΕΜΑΧΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΤΙΜΗ = models.CharField(db_column='ΤΙΜΗ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΣΥΝΟΛΟ = models.CharField(db_column='ΣΥΝΟΛΟ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΣΕΛΙΔΕΣ = models.CharField(db_column='ΣΕΛΙΔΕΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΛΑΤΕΣ = models.CharField(db_column='ΠΕΛΑΤΕΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΗΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΗΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ΦΩΤΟΤΥΠΙΚΑ'

    def __str__(self):
        return f"{self.ΕΤΑΙΡΕΙΑ} ΠΕΡΙΓΡΑΦΗ: {self.ΠΟΙΟΤΗΤΑ} Κωδικός: {self.ΚΩΔΙΚΟΣ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_fototipika', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        return reverse('warehouse:fototipika_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.ID}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())


class ΧΧΧ(models.Model):
    ID = models.AutoField(db_column='ID', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    ΚΩΔΙΚΟΣ = models.CharField(db_column='ΚΩΔΙΚΟΣ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΗΜΕΡΩΜΗΝΙΑ = models.CharField(db_column='ΗΜΕΡΩΜΗΝΙΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΕΡΙΓΡΑΦΗ = models.TextField(db_column='ΠΕΡΙΓΡΑΦΗ', blank=True, null=True)  # Field name made lowercase.
    ΑΠΟΤΕΛΕΣΜΑ = models.CharField(db_column='ΑΠΟΤΕΛΕΣΜΑ', blank=True, null=True, max_length=50)  # Field name made lowercase.
    ΠΑΡΑΤΗΡΗΣΕΙΣ = models.TextField(db_column='ΠΑΡΑΤΗΡΗΣΕΙΣ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ΧΧΧ'

    def __str__(self):
        return f"ΚΩΔΙΚΟΣ: {self.ΚΩΔΙΚΟΣ} ΗΜΕΡΩΜΗΝΙΑ: {self.ΗΜΕΡΩΜΗΝΙΑ} ΠΕΡΙΓΡΑΦΗ: {self.ΠΕΡΙΓΡΑΦΗ}"

    def get_absolute_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:edit_xxx', kwargs={'spare_part_id': self.pk})

    def get_delete_url(self):
        # customers ==>> app name στο urls
        return reverse('warehouse:xxx_delete_product', kwargs={'spare_part_id': self.pk})

    def get_path(self):
        return f'{self._meta.model_name.upper()}/{self.pk}'

    def get_direct_path(self):
        return os.path.join(SPARE_PARTS_URL, self.get_path())
