from django.contrib.gis.db import models
from colorfield.fields import ColorField

# Create your models here.
from region.models import Region


class Province(models.Model):
    id_province = models.AutoField(db_column='idProvincia', primary_key=True)  # Field name made lowercase.
    province = models.CharField(db_column='Provincia', max_length=45)  # Field name made lowercase.
    region_color = ColorField(db_column='provinciacor', default='#FFFF00')
    geography = models.PolygonField(db_column='geography')
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='idRegiao')  # Field name made lowercase.

    def __str__(self):
        return self.province

    class Meta:
        managed = True
        db_table = 'provincia'
