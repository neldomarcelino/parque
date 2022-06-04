from django.contrib import admin
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
# Register your models here.
from region.models import Region


@admin.register(Region)
class GeoAdmin(LeafletGeoAdmin):
    list_display = ('region', 'country')