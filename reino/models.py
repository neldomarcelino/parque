from django.db import models

# Create your models here.


class Reino(models.Model):
    idreino = models.AutoField(db_column='idreino', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=200, db_column="reino")

    class Meta:
        managed = True
        db_table = 'reino'

    def __str__(self):
        return self.descricao
