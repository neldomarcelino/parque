from django.db import models

# Create your models here.
from ordem.models import Ordem


class Familia(models.Model):
    idfamilia = models.AutoField(db_column='idFamilia', primary_key=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=45)  # Field name made lowercase.
    idordem = models.ForeignKey(Ordem, models.DO_NOTHING, db_column='idOrdem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'familia'
