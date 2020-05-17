from django.contrib import admin
from import_export.admin import ImportExportModelAdmin


from warehouse import models as warehouse_models
from django.db.models.base import ModelBase
# Register your models here.


# needed by ImportExportModel
# class A_ΟΡΟΦΟΣAdmin(ImportExportModelAdmin):
#
#     pass

# https://www.protechtraining.com/blog/post/tutorial-using-djangos-multiple-database-support-477

for name, var in warehouse_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)

# admin.site.register(A_ΟΡΟΦΟΣ, A_ΟΡΟΦΟΣAdmin)

