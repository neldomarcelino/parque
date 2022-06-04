import datetime
import calendar

from django.forms import Form
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views import generic

# Create your views here.
from species.models import Specie


@method_decorator(login_required(redirect_field_name='next', login_url='user/login'), name='dispatch')
class Home(generic.DetailView):
    model = Specie
    context_object_name = 'specie'
    template_name = 'index.html'
    this_year = timezone.now()

    def get_object(self, **kwargs):
        dash_species = {
            'all_specie': self.model.objects.all(),
            'this_year': self.get_species_current_year(),
            'last_month': self.get_species_last_month(),
            'last_7_days': self.get_filter_last_7_days(),
        }

        return dash_species

    def get_species_current_year(self):
        """
            Return species for last year
        """

        species = self.get_species_dash(
            datetime.date(year=self.this_year.year, month=1, day=1),
            datetime.date(year=self.this_year.year + 1, month=1, day=1)
        )

        return species

    def get_species_last_month(self):
        """ Return species for last month"""

        month_past_days = timezone.now().day
        last_day_month = calendar.monthrange(timezone.now().year, timezone.now().month)[1]

        species = self.get_species_dash(self.get_date(month_past_days-1),
                datetime.date(year=self.this_year.year,month=self.this_year.month,day=last_day_month))
        return species

    def get_filter_last_7_days(self):
        """ Return species for last 7 days """

        last_7_days = datetime.timedelta(weeks=1).days
        species = self.get_species_dash(self.get_date(last_7_days), self.get_date(-1))
        return species

    def get_species_dash(self, initial_data, second_data):

        return self.model.objects.filter(
            date_created__gte="{}".format(initial_data),
            date_created__lt="{}".format(second_data)
        )

    @staticmethod
    def get_date(days):
        """
            RETURN a day for a week, month and year from today
        """
        today = timezone.now()
        days = datetime.timedelta(days=days)

        return (today - days).date()
