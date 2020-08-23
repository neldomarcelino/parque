from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic
# Create your views here.

from .models import Specie


class IndexView(generic.ListView):
    model = Specie
    template_name = 'species/index.html'
    context_object_name = 'species_list'

    def get_queryset(self):
        """ Return the list of species """
        return Specie.objects.order_by('date_created')


class DetailView(generic.DetailView):
    # specie = get_object_or_404(Especie, pk=id_specie)
    # return render(request, template, {'error_message': 'Specie does not Exist'})
    model = Specie
    context_object_name = 'specie'
    template_name = 'species/detail.html'

