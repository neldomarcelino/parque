from django.db import models

# Create your models here.
from species.models import Specie


class SpecieImage(models.Model):
    id_image = models.AutoField(db_column='idImage', primary_key=True)
    id_specie = models.ForeignKey(Specie, models.CASCADE, db_column='idEspecie', null=False)
    description = models.TextField(db_column='descricao', null=True)
    image = models.FileField(upload_to='image')
    # print(id_specie.)

    class Meta:
        managed = False
        db_table = 'especieimage'
