from django.db import models

# Create your models here.
from district.models import District
from species.models import Specie


class Location(models.Model):
    id_localization = models.AutoField(db_column='idLocalizacao', primary_key=True)  # Field name made lowercase.
    district = models.ForeignKey(District, models.DO_NOTHING, db_column='idDistrito')  # Field name made lowercase.
    specie = models.ForeignKey(Specie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'localizacaoespecie'
        unique_together = (('id_localization', 'district', 'specie'),)

    def __str__(self):
        return self.district.district