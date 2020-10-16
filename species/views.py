import datetime
import calendar
from django.utils import timezone

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import generic
# Create your views here.

from django.views.generic import TemplateView, ListView, DetailView
from .models import Specie


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class IndexView(TemplateView):
    model = Specie
    template_name = 'species/index.html'
    context_object_name = 'results_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = True
        context['header_list'] = self.get_object_header()
        context['filter'] = self.get_filter_date()
        context['results_list'] = self.get_queryset()
        context['list_id'] = context['header_list'].get(0)
        context['header_list'].pop(0)
        this_year = timezone.now()
        print("Tomorrow is: {}".format(datetime.date(year=this_year.year,month=this_year.month,day=31)))
        return context

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
        # return self.model.objects.order_by('date_created')

    def get_object_header(self):
        context = {}
        for field in self.model._meta.fields:
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
            '?date_created__gte={}&date_created__lt={}'.format(self.get_date(1), self.get_date(0)):'Hoje',
            '?date_created__gte={}&date_created__lt={}'.format(self.get_date(week_days),self.get_date(0)):'Último 7 dias',
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
class DetailView(generic.DetailView):
    model = Specie
    context_object_name = 'specie'
    template_name = 'species/detail.html'

    def get_object(self):
        specie = get_object_or_404(Specie, pk=self.kwargs['pk'])
        return specie


