from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils.decorators import method_decorator
from django.views import generic

# Create your views here.


@method_decorator(login_required(redirect_field_name='next', login_url='user/login'), name='dispatch')
class Home(generic.TemplateView):
    template_name = 'home/base.html'





