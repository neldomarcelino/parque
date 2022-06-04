from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView

from species.models import Specie
from .models import Geography


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class IndexView(TemplateView):
    model = Geography
    template_name = 'geography/geomap.html'
    context_object_name = 'results_list'


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class SpecieDetailView(DetailView):
    model = Geography
    template_name = 'geography/geomap.html'
    context_object_name = 'result_data'


def get_specie_map(request):
    data = serialize('geojson', Geography.objects.all())
    return HttpResponse(data, content_type='json')
