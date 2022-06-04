from django.contrib import admin

# Register your models here.
from .models import Identifier


class IdentifierAdmin(admin.ModelAdmin):
    list_display = ['person', 'specie']


admin.site.register(Identifier, IdentifierAdmin)
