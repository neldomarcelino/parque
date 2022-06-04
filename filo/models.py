from django.db import models

# Create your models here.
from reino.models import Reino


class Filo(models.Model):
    idfilo = models.AutoField(db_column='idFilo', primary_key=True)  # Field name made lowercase.
    filo = models.CharField(db_column='Filo', max_length=45)  # Field name made lowercase.
    idreino = models.ForeignKey(Reino, models.DO_NOTHING, db_column='idReino', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'filo'

    def __str__(self):
        return self.filo
