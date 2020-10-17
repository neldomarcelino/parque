from django.conf.urls import url
from django.urls import path

from geography import views

app_name = 'geography'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]