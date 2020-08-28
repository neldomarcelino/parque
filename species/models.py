import datetime

from django.db import models
from django.utils import timezone
#from django.contrib.gis.geos import Point

from genero.models import Genero
# Create your models here.


class Specie(models.Model):
    id_specie = models.AutoField(db_column='idspecie', primary_key=True)  # Field name made lowercase.
    specie = models.CharField(db_column='specie', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gender = models.ForeignKey(Genero, models.DO_NOTHING, db_column='idGenero', blank=True, null=False)  # Field name made lowercase.
    habitat = models.CharField(db_column='Habitat', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    detail = models.CharField(db_column='detalhes', max_length=1000, blank=True, null=True)
    common_name = models.CharField(db_column='NomeComum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    date_created = models.DateTimeField(db_column='DataCriacao')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'specie'

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=2) <= self.date_created <= now

    def __str__(self):
        return self.specie