from django.contrib import admin

from .models import Calendar
from import_export.admin import ImportExportModelAdmin


# needed by ImportExportModel
class CalendarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['Ημερομηνία', 'Πελάτης', 'Copier_ID', 'Σκοπός']

    class Meta:
        model = Calendar


admin.site.register(Calendar, CalendarAdmin)
# Register your models here.

# Register your models here.
