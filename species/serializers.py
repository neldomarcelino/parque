from rest_framework import serializers

from species.models import Specie


class SpecieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Specie
        fields = ['specie', 'habitat', 'detail', 'common_name', 'date_created', 'year']
