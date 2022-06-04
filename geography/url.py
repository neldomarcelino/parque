from django.conf.urls import url
from django.urls import path

from geography import views

app_name = 'geography'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('specie/<int:id>', views.IndexView.as_view(), name='specie'),
    url(r'^speciegeodata/$', views.get_specie_map, name='speciegeo'),
    path('regions/', views.IndexView.as_view(), name='regions'),
]