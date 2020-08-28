from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
# Create your views here.
from django.views.generic import TemplateView

from .models import Specie


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class IndexView(TemplateView):
    model = Specie
    template_name = 'species/index.html'
    #context_object_name = 'results'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result_headers'] = {'Data', 'Genero', 'Habitat', 'Nome Comum', 'Especie'}
        context['results'] = Specie.objects.all()[:5]
        return context

    def get_queryset(self):
        """ Return the list of species """
        return Specie.objects.order_by('date_created')


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class DetailView(generic.DetailView):
    # specie = get_object_or_404(Especie, pk=id_specie)
    # return render(request, template, {'error_message': 'Specie does not Exist'})
    model = Specie
    context_object_name = 'specie'
    template_name = 'species/detail.html'

