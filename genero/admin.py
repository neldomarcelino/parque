from django.contrib import admin

# Register your models here.
from .models import Genero


class GenderAdmin(admin.ModelAdmin):
    list_display = ('genero', 'idfamilia')


admin.site.register(Genero)