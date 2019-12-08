from django.db import models

# Create your models here.


class Reino(models.Model):
    idreino = models.AutoField(db_column='idReino', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'reino'

    def __str__(self):
        return self.descricao
