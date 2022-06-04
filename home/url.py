from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


from species.views import SpecieDashView
from home.views import Home

app_name = 'home'
urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('', SpecieDashView.as_view(), name="dashspecie")
]