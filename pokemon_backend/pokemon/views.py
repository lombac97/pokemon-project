from pickle import TRUE
from django.shortcuts import render
from pokemon.listing_serializers import AbilitiesListingField, AreasListingField, LocationsListingField, MovesListingField, PokemonAreasListingField, StatsListingField, TypesListingField
from pokemon.models import Ability, Area, Location, Pokemon, PokemonAbility, Region
from pokemon.output_serializers import SpriteOutputSerializer
from pokemon.serializer import RegionSerializer, SpriteSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import NotFound
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
        except Exception as e:
            raise e


class RegionsList(APIView):
    def get(self, request):
        regions = Region.objects.all()
        regions_serializer = RegionSerializer(regions, many=True)
        return Response(regions_serializer.data)


class RegionDetails(APIView):
    class OutputSerializer(serializers.ModelSerializer):
        locations = LocationsListingField(many=True, read_only=True)

        class Meta:
            model = Region
            fields = "__all__"

    def get(self, request, pk):
        try:
            region = Region.objects.get(pk=pk)
            region_serializer = self.OutputSerializer(instance=region)
            return Response(region_serializer.data)

        except Region.DoesNotExist:
            raise NotFound("Region not found")
        except Exception as e:
            raise e


class LocationDetails(APIView):
    class OutputSerializer(serializers.ModelSerializer):
       # locations = LocationsListingField(many=True, read_only=True)
        areas = AreasListingField(many=True, read_only=True)

        class Meta:
            model = Location
            fields = "__all__"

    def get(self, request, pk):
        try:
            location = Location.objects.get(pk=pk)
            location_serializer = self.OutputSerializer(instance=location)
            return Response(location_serializer.data)

        except Location.DoesNotExist:
            raise NotFound("Location not found")
        except Exception as e:
            raise e


class AreaDetails(APIView):
    class OutputSerializer(serializers.ModelSerializer):
       # locations = LocationsListingField(many=True, read_only=True)
      #  areas = AreasListingField(many=True, read_only=True)
        pokemons = PokemonAreasListingField(many=True, read_only=True)

        class Meta:
            model = Area
            fields = "__all__"

    def get(self, request, pk):
        try:
            area = Area.objects.get(pk=pk)
            area_serializer = self.OutputSerializer(instance=area)
            return Response(area_serializer.data)
        except Area.DoesNotExist:
            raise NotFound("Area not found")
        except Exception as e:
            raise e
