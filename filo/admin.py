from django.contrib import admin

# Register your models here.

from .models import Filo


class FiloAdmin(admin.ModelAdmin):
    list_display = ('filo', 'idreino')


admin.site.register(Filo)