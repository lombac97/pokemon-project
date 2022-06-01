from .models import Location, PokemonType, Region, Pokemon, PokemonArea, Sprite, Area, Ability, Move, Stat, Storage, Type, PokemonAbility, PokemonMove

from rest_framework import serializers


# Creation List Serializers

class PokemonMoveCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        pokemon_moves = [PokemonMove(**item) for item in validated_data]
        return PokemonMove.objects.bulk_create(pokemon_moves)


class MoveCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        moves = [Move(**item) for item in validated_data]
        return Move.objects.bulk_create(moves)


class PokemonTypeCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        pokemon_types = [PokemonType(**item) for item in validated_data]
        return PokemonType.objects.bulk_create(pokemon_types)


class PokemonAreaCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        pokemon_areas = [PokemonArea(**item) for item in validated_data]
        return PokemonArea.objects.bulk_create(pokemon_areas)


class PokemonAbilityCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        pokemon_abilities = [PokemonAbility(**item) for item in validated_data]
        return PokemonAbility.objects.bulk_create(pokemon_abilities)


class TypeCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        types = [Type(**item) for item in validated_data]
        return Type.objects.bulk_create(types)


class LocationCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        locations = [Location(**item) for item in validated_data]

        return Location.objects.bulk_create(locations)


class RegionCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):

        regions = [Region(**item) for item in validated_data]

        return Region.objects.bulk_create(regions)


class StatCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        stats = [Stat(**item) for item in validated_data]
        return Stat.objects.bulk_create(stats)


class AreaCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        areas = [Area(**item) for item in validated_data]
        return Area.objects.bulk_create(areas)


class AbilityCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        abilities = [Ability(**item) for item in validated_data]
        return Ability.objects.bulk_create(abilities)


# Model Serializers

class SpriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprite
        fields = "__all__"


class PokemonSerializer(serializers.ModelSerializer):
    sprite_id = SpriteSerializer(read_only=True)

    class Meta:
        model = Pokemon
        fields = "__all__"


class MoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Move
        list_serializer_class = MoveCreateListSerializer
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        list_serializer_class = TypeCreateListSerializer
        fields = "__all__"


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        list_serializer_class = StatCreateListSerializer
        fields = "__all__"


class AbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ability
        list_serializer_class = AbilityCreateListSerializer
        fields = "__all__"


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        list_serializer_class = AreaCreateListSerializer
        fields = "__all__"


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


class StorageSerializer(serializers.ModelSerializer):
    pokemon_id = PokemonSerializer(read_only=True)

    class Meta:
        model = Storage
        fields = "__all__"


class PokemonAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonArea
        list_serializer_class = PokemonAreaCreateListSerializer
        fields = "__all__"


class PokemonAbilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonAbility
        list_serializer_class = PokemonAbilityCreateListSerializer
        fields = "__all__"


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        list_serializer_class = PokemonTypeCreateListSerializer
        fields = "__all__"


class PokemonMoveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonMove
        list_serializer_class = PokemonMoveCreateListSerializer
        fields = "__all__"
