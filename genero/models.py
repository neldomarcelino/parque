from django.db import models

# Create your models here.
from familia.models import Familia

class Genero(models.Model):
    idgenero = models.AutoField(db_column='idGenero', primary_key=True)  # Field name made lowercase.
    genero = models.CharField(db_column='genero', max_length=45)  # Field name made lowercase.
    idfamilia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='idFamilia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'genero'

    def __str__(self):
        return self.genero