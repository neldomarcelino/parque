from django.db import models

# Create your models here.
from province.models import Province


class District(models.Model):
    id_district = models.AutoField(db_column='idDistrito', primary_key=True)  # Field name made lowercase.
    district = models.CharField(db_column='Distrito', max_length=45)  # Field name made lowercase.
    province = models.ForeignKey(Province, models.DO_NOTHING, db_column='idProvincia')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'distrito'
