from django.contrib import admin

from .models import ServiceData
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class ServiceDataAdmin(ImportExportModelAdmin):
    pass


admin.site.register(ServiceData, ServiceDataAdmin)
# Register your models here.

# Register your models here.
