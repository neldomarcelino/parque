from django.contrib import admin

# Register your models here.
from .models import Actor


class ActorAdmin(admin.ModelAdmin):
    list_display = ['person', 'specie']


admin.site.register(Actor, ActorAdmin)