from .models import Area, Location, Region

from rest_framework import serializers


# Creation List Serializers


class RegionCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):

        regions = [Region(**item) for item in validated_data]

        return Region.objects.bulk_create(regions)


class LocationCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        locations = [Location(**item) for item in validated_data]

        return Location.objects.bulk_create(locations)


class AreaCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        areas = [Area(**item) for item in validated_data]
        return Area.objects.bulk_create(areas)


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        list_serializer_class = RegionCreateListSerializer
        fields = ["id", "name"]


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        list_serializer_class = LocationCreateListSerializer
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        list_serializer_class = AreaCreateListSerializer
        fields = "__all__"
