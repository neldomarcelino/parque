from django.contrib import admin

# Register your models here.
from .models import Classe


class ClassAdmin(admin.ModelAdmin):
    list_display = ('classe', 'idfilo')


admin.site.register(Classe, ClassAdmin)