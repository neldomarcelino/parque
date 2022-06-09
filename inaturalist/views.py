from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView
from pyinaturalist import get_observations

from inaturalist.models import iNaturalist


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class iNaturalistView(TemplateView):
    model = iNaturalist
    template_name = 'inaturalist/inaturalist_list.html'
    context_object_name = 'results_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results_list'] = self.i_observations_by_user()
        for inaturalist in self.i_observations_by_user()['results']:
            print("TESTE:{}".format(inaturalist))

        return context

    def i_observations_by_user(self):
        # inaturalist = get_object_or_404(iNaturalist, user_id=self.kwargs['iusername'])
        observations = get_observations(user_id='guerzeneldo')
        return observations

    def i_authenticate(self):
        token = {
            'username': '',
            'password': '',
            'app_id': 'my_app_id',
            'app_secret': '',
        }