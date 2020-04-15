from django.contrib import admin
from . models import Machines
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class MachinesAdmin(ImportExportModelAdmin):
    verbose_name_plural = 'Φωτοτυπικά'
    pass


admin.site.register(Machines, MachinesAdmin)

