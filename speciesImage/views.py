from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator

from speciesImage.models import SpecieImage



@method_decorator(login_required(redirect_field_name='next', login_url='/user/login'), name='dispatch')
class AddSpecieImag:
    model = SpecieImage
    context_object_name = 'specie'
    template_name = 'species/specie_add.html'
    # form_class = ImageSpecieCreateForm
    success_url = '/'
