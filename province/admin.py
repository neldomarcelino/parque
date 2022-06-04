from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin
# Register your models here.
from province.models import Province


@admin.register(Province)
class GeoAdmin(LeafletGeoAdmin):
    list_display = ('province', 'region')