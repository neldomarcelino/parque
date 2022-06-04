from django.contrib import admin

# Register your models here.
# from geography.models import Geography
from geography.models import Geography
from location.models import Location
from species.models import Specie
from actor.models import Actor
from identifier.models import Identifier


class PersonInline(admin.StackedInline):
    model = Actor
    extra = 1


class IdentifierInline(admin.StackedInline):
    model = Identifier
    extra = 1


class LocationInline(admin.TabularInline):
    model = Location
    extra = 1


class GeographyInline(admin.TabularInline):
    model = Geography
    extra = 1
    max_num = 1
    fields = ['description', 'location']


@admin.register(Specie)
class SpecieAdmin(admin.ModelAdmin):
    list_display = ('specie', 'habitat', 'detail', 'common_name', 'gender', 'date_created', 'year')
    list_filter = ['habitat', 'date_created', 'gender']
    search_fields = ['specie', 'common_name']
    list_per_page = 10
    fieldsets = [
        (None, {'fields': ['specie']}),
        (None, {'fields': ['common_name']}),
        (None, {'fields': ['habitat']}),
        (None, {'fields': ['detail']}),
        (None, {'fields': ['gender']}),
        ('Date Information', {'fields': ['date_created', 'year']})
    ]
    inlines = [GeographyInline, PersonInline, IdentifierInline]
    # inlines = [PersonInline, IdentifierInline]




