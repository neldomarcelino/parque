from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import generic

# Create your views here.


class Home(generic.TemplateView):
    template_name = 'home/base.html'



