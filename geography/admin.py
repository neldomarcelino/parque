from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
# Register your models here.

from .models import Geography


@admin.register(Geography)
class GeoAdmin(OSMGeoAdmin):
    list_display = ('specie', 'description', 'longitude', 'latitude')
    search_fields = ['specie']


