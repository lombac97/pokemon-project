from .models import PokemonType, Pokemon, PokemonArea, Sprite,  Ability, Move, Stat, Storage, Type, PokemonAbility, PokemonMove

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


class StatCreateListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        stats = [Stat(**item) for item in validated_data]
        return Stat.objects.bulk_create(stats)


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


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = "__all__"
