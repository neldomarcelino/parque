from django.db import models

# Create your models here.


class Person(models.Model):
    id_person = models.AutoField(db_column='idPessoa', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'pessoa'

    def __str__(self):
        return self.name