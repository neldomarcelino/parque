from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
# Register your models here.
from district.models import District


@admin.register(District)
class GeoAdmin(LeafletGeoAdmin):
    list_display = ('district', 'province')