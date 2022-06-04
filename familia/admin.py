from django.contrib import admin

# Register your models here.

from .models import Familia


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('familia', 'idordem')


admin.site.register(Familia, FamilyAdmin)