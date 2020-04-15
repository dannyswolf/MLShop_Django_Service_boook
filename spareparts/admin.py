from django.contrib import admin

from .models import SpareParts
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class SparePartsAdmin(ImportExportModelAdmin):
    pass


admin.site.register(SpareParts, SparePartsAdmin)
