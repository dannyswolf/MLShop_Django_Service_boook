from django.contrib import admin
from .models import Services
from import_export.admin import ImportExportModelAdmin

# Register your models here.


# needed by ImportExportModel
class ServicesAdmin(ImportExportModelAdmin):

    pass


admin.site.register(Services, ServicesAdmin)

