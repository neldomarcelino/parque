from django.db import models

# Create your models here.
from classe.models import Classe


class Ordem(models.Model):
    idordem = models.AutoField(db_column='idOrdem', primary_key=True)  # Field name made lowercase.
    ordem = models.CharField(db_column='Ordem', max_length=45)  # Field name made lowercase.
    idclasse = models.ForeignKey(Classe, models.DO_NOTHING, db_column='idClasse', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ordem'
