from django.contrib import admin

from .models import ReceiverEmails
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class ReceiverEmailAdmin(ImportExportModelAdmin):
    pass


admin.site.register(ReceiverEmails, ReceiverEmailAdmin)
# Register your models here.

# Register your models here.
