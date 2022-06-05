import datetime

from django.contrib.gis.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.gis.geos import Point

from genero.models import Genero
# Create your models here.


class iNaturalist(models.Model):
    pass