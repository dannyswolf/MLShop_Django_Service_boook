from django.contrib import admin
from . models import CopiersLog
from import_export.admin import ImportExportModelAdmin
# Register your models here.


class CopiersLogAdmin(ImportExportModelAdmin):
    verbose_name_plural = 'Ιστορικό μεταφορών'


admin.site.register(CopiersLog, CopiersLogAdmin)

