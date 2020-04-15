from django.contrib import admin

from .models import Companies
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class CompaniesAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Companies, CompaniesAdmin)
