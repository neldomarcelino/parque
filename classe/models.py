from django.db import models

# Create your models here.
from filo.models import Filo


class Classe(models.Model):
    idclasse = models.AutoField(db_column='idClasse', primary_key=True)  # Field name made lowercase.
    classe = models.CharField(db_column='Classe', max_length=45)  # Field name made lowercase.
    idfilo = models.ForeignKey(Filo, models.DO_NOTHING, db_column='idFilo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'classe'
