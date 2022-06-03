
from places.listing_serializers import AreasListingField, LocationsListingField
from pokemon.listing_serializers import PokemonAreasListingField
from .models import Area, Location, Region

from .serializer import RegionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import NotFound


class RegionsList(APIView):
    """
    Lists all regions in the database

    Methods
    -------
    get(request, pk)
        Lists all regions in the database

    """

    def get(self, request):

        regions = Region.objects.all()
        regions_serializer = RegionSerializer(regions, many=True)
        return Response(regions_serializer.data)


class RegionDetails(APIView):
    """
    Lists an specific region with its locations

    Methods
    -------
    get(request, pk)
        Lists an specific region with its locations

    """

    class OutputSerializer(serializers.ModelSerializer):
        locations = LocationsListingField(many=True, read_only=True)

        class Meta:
            model = Region
            fields = "__all__"

    def get(self, request, pk):
        """
        Parameters
        ----------
        pk: Region id in the database

        Raises
        ------
        Region.DoesNotExist
            If the region does not exist in the database
        """
        try:
            region = Region.objects.get(pk=pk)
            region_serializer = self.OutputSerializer(instance=region)
            return Response(region_serializer.data)

        except Region.DoesNotExist:
            raise NotFound("Region not found")


class LocationDetails(APIView):
    """
    Lists an specific Location with its areas

    Methods
    -------
    get(request, pk)
        Lists an specific Location with its areas

    """
    class OutputSerializer(serializers.ModelSerializer):

        areas = AreasListingField(many=True, read_only=True)

        class Meta:
            model = Location
            fields = "__all__"

    def get(self, request, pk):
        """
        Parameters
        ----------
        pk: Location id in the database

        Raises
        ------
        Location.DoesNotExist
            If the location does not exist in the database
        """

        try:
            location = Location.objects.get(pk=pk)
            location_serializer = self.OutputSerializer(instance=location)
            return Response(location_serializer.data)

        except Location.DoesNotExist:
            raise NotFound("Location not found")


class AreaDetails(APIView):
    """
    Lists an specific Area with its pokemons

    Methods
    -------
    get(request, pk)
        Lists an specific Area with its pokemons

    """

    class OutputSerializer(serializers.ModelSerializer):
        pokemons = PokemonAreasListingField(many=True, read_only=True)

        class Meta:
            model = Area
            fields = "__all__"

    def get(self, request, pk):
        """
        Parameters
        ----------
        pk: Area id in the database

        Raises
        ------
        Area.DoesNotExist
            If the area does not exist in the database
        """

        try:
            area = Area.objects.get(pk=pk)
            area_serializer = self.OutputSerializer(instance=area)
            return Response(area_serializer.data)
        except Area.DoesNotExist:
            raise NotFound("Area not found")
