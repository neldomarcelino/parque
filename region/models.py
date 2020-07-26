from django.db import models

# Create your models here.


class Region(models.Model):
    id_region = models.AutoField(db_column='idRegiao', primary_key=True)  # Field name made lowercase.
    region = models.CharField(db_column='Regiao', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'regiao'
