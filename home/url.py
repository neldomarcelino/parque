from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


from . import views

app_name = 'home'
urlpatterns = [
    path('', views.Home.as_view(), name='index'),
]