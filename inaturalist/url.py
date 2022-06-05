from django.urls import path

from inaturalist.views import iNaturalistView

app_name = 'inaturalist'
urlpatterns = [
    path('', iNaturalistView.as_view(), name='inaturalist'),
]