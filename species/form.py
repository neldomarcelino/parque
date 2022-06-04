from django.forms import ModelForm

from species.models import Specie


class SpecieCreateForm(ModelForm):
    class Meta:
        model = Specie
        fields = ['specie', 'date_created', 'common_name', 'threat', 'year', 'detail', 'habitat', 'specie_image']