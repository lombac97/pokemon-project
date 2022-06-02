from pokemon.listing_serializers import AbilitiesListingField, MovesListingField, StatsListingField, TypesListingField
from pokemon.models import Pokemon
from pokemon.output_serializers import SpriteOutputSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class PokemonInfo(APIView):

    class OutputSerializer(serializers.ModelSerializer):
        abilities = AbilitiesListingField(many=True, read_only=True)
        types = TypesListingField(many=True, read_only=True)
        moves = MovesListingField(many=True, read_only=True)
        stats = StatsListingField(many=True, read_only=True)
        sprite = SpriteOutputSerializer()

        class Meta:
            model = Pokemon
            fields = "__all__"

    def get(self, request, pk):
        try:
            pokemon = Pokemon.objects.get(pk=pk)
            pokemon_serializer = self.OutputSerializer(instance=pokemon)
            return Response(pokemon_serializer.data)
        except Pokemon.DoesNotExist:
            raise NotFound("Pokemon not found")


class OwnPokemonInfo(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        print("Hola")
