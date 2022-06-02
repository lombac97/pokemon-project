
from pokemon.output_serializers import PokemonFromAreaOutputSerializer
from rest_framework import serializers


class LocationsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {"id": value.id, "name": value.name}


class AreasListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {'id': value.id, 'name': value.name, 'pokemon_count': value.pokemon_count, 'location': value.location.id}
