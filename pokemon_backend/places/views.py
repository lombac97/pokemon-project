
from places.listing_serializers import AreasListingField, LocationsListingField
from pokemon.listing_serializers import PokemonAreasListingField
from .models import Area, Location, Region

from .serializer import RegionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import NotFound


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
