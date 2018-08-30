from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import SuperGroup

# Register your models here.
@admin.register(SuperGroup)
class SuperGroupAdmin(ImportExportModelAdmin):
    pass