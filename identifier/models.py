from django.db import models

# Create your models here.
from person.models import Person
from species.models import Specie


class Identifier(models.Model):
    person = models.OneToOneField(Person, models.DO_NOTHING, db_column='idPessoa', primary_key=True)  # Field name made lowercase.
    specie = models.ForeignKey(Specie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'quemidentificou'
        unique_together = (('person', 'specie'),)

    def __str__(self):
        return self.person.name