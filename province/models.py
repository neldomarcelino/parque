from django.db import models

# Create your models here.
from region.models import Region


class Province(models.Model):
    id_province = models.AutoField(db_column='idProvincia', primary_key=True)  # Field name made lowercase.
    province = models.CharField(db_column='Provincia', max_length=45)  # Field name made lowercase.
    region = models.ForeignKey(Region, models.DO_NOTHING, db_column='idRegiao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provincia'
