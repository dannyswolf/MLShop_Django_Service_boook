from django.contrib import admin
from .models import Customer
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class CustomersAdmin(ImportExportModelAdmin):
    pass


admin.site.register(Customer, CustomersAdmin)
# Register your models here.

