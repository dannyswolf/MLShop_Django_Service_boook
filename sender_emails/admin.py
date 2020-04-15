from django.contrib import admin

from .models import SenderEmails
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class SenderEmailAdmin(ImportExportModelAdmin):
    pass


admin.site.register(SenderEmails, SenderEmailAdmin)
# Register your models here.

# Register your models here.
