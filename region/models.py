from django.contrib.gis.db import models
from colorfield.fields import ColorField
# Create your models here.


class Region(models.Model):
    id_region = models.AutoField(db_column='idRegiao', primary_key=True)  # Field name made lowercase.
    region = models.CharField(db_column='Regiao', max_length=45)  # Field name made lowercase.
    region_color = ColorField(db_column='regiaocor', default='#FF0000')
    geography = models.PolygonField(db_column='geography')
    country = models.CharField(db_column='pais', null=True, max_length=100)

    def __str__(self):
        return self.region

    class Meta:
        managed = True
        db_table = 'regiao'
