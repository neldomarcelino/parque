import datetime
import calendar

from django.forms import Form
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
# Create your views here.

from django.views.generic import TemplateView

from ordem.models import Ordem
from classe.models import Classe
from filo.models import Filo
from genero.models import Genero
from reino.models import Reino
from familia.models import Familia

from speciesImage.models import SpecieImage
from . import dashplotly
from .form import SpecieCreateForm
from .models import Specie

# Rest full API
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import SpecieSerializer


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class IndexView(TemplateView):
    model = Specie
    template_name = 'species/specie_list.html'
    context_object_name = 'results_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = True
        context['filter'] = self.get_filter_date()
        context['results_list'] = self.get_queryset()

        return context

    def get_images(self):
        specie = get_object_or_404(Specie, pk=self.kwargs['pk'])
        data = SpecieImage.objects.filter(id_specie=specie.id_specie)
        return data

    def get_videos(self):
        specie = get_object_or_404(Specie, pk=self.kwargs['pk'])
        data = SpecieImage.objects.filter(id_specie=specie.id_specie)
        return data

    def get_audios(self):
        specie = get_object_or_404(Specie, pk=self.kwargs['pk'])
        data = SpecieImage.objects.filter(id_specie=specie.id_specie)
        return data

    def get_queryset(self):
        """ Return the list of species """
        query_search = self.request.GET.get('q') if self.request.GET.get('q') is not None else ""
        date_created_gte = self.request.GET.get('date_created__gte') \
            if self.request.GET.get('date_created__gte') is not None else datetime.date.min
        date_created_lt = self.request.GET.get('date_created__lt') \
            if self.request.GET.get('date_created__lt') is not None else datetime.date.max

        return self.model.objects.filter(
            specie__icontains=query_search,
            detail__icontains=query_search,
            date_created__gte=date_created_gte,
            date_created__lt=date_created_lt
        )

    def get_object_header(self):
        context = {}
        for field in self.model._meta.fields:
            if field.name is not "year":
                if field.name is not "threat":
                    context.update({len(context): field.name})

        return context

    def get_filter_date(self):
        """ Return data query for filter """
        week_days = datetime.timedelta(weeks=1).days
        month_past_days = timezone.now().day
        last_day_month = calendar.monthrange(timezone.now().year, timezone.now().month)[1]
        this_year = timezone.now()

        context = {
            '?o=':'Qualquer Período',
            '?date_created__gte={}&date_created__lte={}'.format(self.get_date(1), self.get_date(0)):'Hoje',
            '?date_created__gte={}&date_created__lte={}'.format(self.get_date(week_days),self.get_date(0)):'Último 7 dias',
            '?date_created__gte={}&date_created__lt={}'.format(
                self.get_date(month_past_days-1),
                datetime.date(year=this_year.year,month=this_year.month,day=last_day_month)
            ):'Este Mês',
            '?date_created__gte={}&date_created__lt={}'.format(
                datetime.date(year=this_year.year,month=1,day=1)
                ,datetime.date(year=this_year.year+1, month=1,day=1))
            : 'Este Ano'
        }
        return context

    @staticmethod
    def get_date(days):
        """
            RETURN a day for a week, month and year from today
        """
        today = timezone.now()
        days = datetime.timedelta(days=days)

        return (today - days).date()


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class ClassificationView(TemplateView):
    model = Specie
    template_name = 'species/specie_filter.html'
    context_object_name = 'results_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reino'] = Reino.objects.all()
        context['filo'] = Filo.objects.all()
        context['classe'] = Classe.objects.all()
        context['ordem'] = Ordem.objects.all()
        context['familia'] = Familia.objects.all()
        context['genero'] = Genero.objects.all()

        return context


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class DeleteView(generic.edit.DeleteView):
    model = Specie
    success_url = reverse_lazy('species:index')


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class UpdateView(generic.UpdateView):
    model = Specie
    fields = ['specie', 'common_name', 'detail', 'habitat']
    template_name_suffix = '_update'


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class DetailView(generic.DetailView):
    model = Specie
    context_object_name = 'specie'
    template_name = 'species/specie_view.html'

    def get_object(self):
        specie = get_object_or_404(Specie, pk=self.kwargs['pk'])
        return specie


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class AddView(generic.CreateView):
    model = Specie
    context_object_name = 'specie'
    template_name = 'species/specie_add.html'
    form_class = SpecieCreateForm


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class SpecieDashView(IndexView):
    model = Specie
    context_object_name = 'specie'
    template_name = "species/specie_dash.html"

    def get_object(self):
        specie = get_object_or_404(Specie, pk=self.kwargs['pk'])
        return specie


class DashSpeciesQuery:

    def dash_species_per_year(self):
        species = Specie.objects.all()
        return species


class SpecieViewSetAPI(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Specie.objects.all().order_by('-date_created')
    serializer_class = SpecieSerializer
    permission_classes = [permissions.IsAuthenticated]


# @method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
# class AddSpecieImag:
#     model = SpecieImage
#     context_object_name = 'images_specie'
#     template_name = 'species/specie_add.html'
#     # form_class = ImageSpecieCreateForm
#     success_url = '/'
#
#     def get_name(self, request):
#         # if this is a POST request we need to process the form data
#         if request.method == 'POST':
#             self.model.image = ''


