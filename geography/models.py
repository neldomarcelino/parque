from django.contrib.gis.db import models
# Create your models here.
from species.models import Specie


class Geography(models.Model):
    id_geometry = models.AutoField(primary_key=True, db_column='idgeo')
    description = models.CharField(db_column='description', max_length=1000, blank=True, null=True)
    location = models.MultiPointField(db_column='location')
    specie = models.ForeignKey(Specie, models.DO_NOTHING, db_column='idEspecie', blank=True, null=False)
    latitude = models.DecimalField(db_column='latitude', max_digits=100, decimal_places=2)
    longitude = models.DecimalField(db_column='longitude', max_digits=100, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'geography'

    def __str__(self):
        return self.specie.specie