from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from .models import Geography


@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class IndexView(TemplateView):
    model = Geography
    template_name = 'geography/geomap.html'
    context_object_name = 'results_list'
