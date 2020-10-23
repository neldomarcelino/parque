from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'species'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<str:q>', views.IndexView.as_view(), name='search'),
    url(r'^(?P<str>)/$', views.IndexView.as_view(), name='search'),
    path('detail/<int:pk>', views.DetailView.as_view(), name="detail"),
    path('add_specie/', views.AddView.as_view(), name="addspecie"),
    path('dash_specie/', views.SpecieDashView.as_view(), name="dashspecie")
]