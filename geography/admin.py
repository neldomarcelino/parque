from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin, LeafletGeoAdminMixin

# Register your models here.

from .models import Geography
from django.contrib.gis.db import models as geo_models

# Create your models here.
from leaflet.forms.widgets import LeafletWidget

from species.models import Specie

LEAFLET_WIDGET_ATTRS = {
    'map_height': '500px',
    'map_width': '100%',
    'display_raw': 'true',
    'map_srid': 4326,
}

LEAFLET_FIELD_OPTIONS = {'widget': LeafletWidget(attrs=LEAFLET_WIDGET_ATTRS)}

FORMFIELD_OVERRIDES = {
    geo_models.PointField: LEAFLET_FIELD_OPTIONS,
    geo_models.MultiPointField: LEAFLET_FIELD_OPTIONS,
    geo_models.LineStringField: LEAFLET_FIELD_OPTIONS,
    geo_models.MultiLineStringField: LEAFLET_FIELD_OPTIONS,
    geo_models.PolygonField: LEAFLET_FIELD_OPTIONS,
    geo_models.MultiPolygonField: LEAFLET_FIELD_OPTIONS,
}


@admin.register(Geography)
class GeoAdmin(LeafletGeoAdmin):
    list_display = ('specie', 'description', 'longitude', 'latitude')
    search_fields = ['specie']
    formfield_overrides = FORMFIELD_OVERRIDES


