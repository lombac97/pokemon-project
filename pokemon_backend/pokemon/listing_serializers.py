
from pokemon.output_serializers import PokemonFromAreaOutputSerializer
from rest_framework import serializers


class AbilitiesListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.ability.name


class TypesListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.type.name


class MovesListingField(serializers.RelatedField):
    def to_representation(self, value):
        return value.move.name


class StatsListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {"name": value.name, "value": value.value}


class PokemonAreasListingField(serializers.RelatedField):
    def to_representation(self, value):
        return PokemonFromAreaOutputSerializer(instance=value.pokemon).data
