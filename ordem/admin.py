from django.contrib import admin

# Register your models here.

from .models import Ordem


class OrdemAdmin(admin.ModelAdmin):
    list_display = ('ordem', 'idclasse')


admin.site.register(Ordem)