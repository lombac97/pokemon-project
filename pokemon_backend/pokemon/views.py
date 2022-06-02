from http import HTTPStatus
from pokemon.listing_serializers import AbilitiesListingField, MovesListingField, PokemonStoragesListingField, StatsListingField, TypesListingField
from pokemon.models import Pokemon, Storage
from pokemon.output_serializers import SpriteOutputSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.exceptions import NotFound, ParseError, ValidationError
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from pokemon.serializer import StorageSerializer
from pokemon.services import catch_pokemon, delete_storage_pokemon, edit_pokemon, enter_pokemon_party, get_user_party_pokemons, leave_pokemon_party, swap_pokemon_party, validate_both_swap_fields
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

    class InputSerializer(serializers.Serializer):
        specie = serializers.IntegerField()
        nick_name = serializers.CharField()
        is_party_member = serializers.BooleanField()

    class GetOutputSerializer(serializers.ModelSerializer):
        specie = PokemonStoragesListingField(read_only=True)

        class Meta:
            model = Storage
            fields = ["id", "nick_name", "is_party_member", "specie"]

    class EditInputSerializer(serializers.Serializer):
        nick_name = serializers.CharField()

    def get(self, request):
        try:
            storages = Storage.objects.filter(user=request.user)
            storages_serializer = self.GetOutputSerializer(
                many=True, instance=storages)
            if(len(storages_serializer.data) == 0):
                return Response({"details": "No pokemons have been found"})

            return Response(storages_serializer.data)

        except User.DoesNotExist:
            raise NotFound("User not found")

    def post(self, request):
        try:
            input_data = self.InputSerializer(data=request.data)
            input_data.is_valid(raise_exception=True)
            save_data = catch_pokemon(input_data.data, request.user.id)
            save_data.pop("user")
            return Response(save_data, HTTPStatus.CREATED)
        except ValidationError:
            raise ParseError("Invalid data")

    def put(self, request, pk):
        try:
            input_data = self.EditInputSerializer(data=request.data)
            input_data.is_valid(raise_exception=True)
            save_data = edit_pokemon(input_data.data, request.user.id, pk)
            storage_serializer = StorageSerializer(instance=save_data)
            data = storage_serializer.data
            data.pop("user")
            return Response(data)
        except ValidationError:
            raise ParseError("Invalid data")
        except Storage.DoesNotExist:
            raise NotFound("Pokemon not found")

    def patch(self, request, pk):
        try:
            input_data = self.EditInputSerializer(data=request.data)
            input_data.is_valid(raise_exception=True)
            save_data = edit_pokemon(input_data.data, request.user.id, pk)
            storage_serializer = StorageSerializer(instance=save_data)
            data = storage_serializer.data
            data.pop("user")
            return Response(data)
        except ValidationError:
            raise ParseError("Invalid data")
        except Storage.DoesNotExist:
            raise NotFound("Pokemon not found")

    def delete(self, request, pk):
        try:
            delete_storage_pokemon(pk, request.user.id)
            return Response(None, HTTPStatus.NO_CONTENT)
        except ValidationError:
            raise ParseError("Invalid data")
        except Storage.DoesNotExist:
            raise NotFound("Pokemon not found")


class OwnPokemonPartyInfo(APIView):
    permission_classes = [IsAuthenticated]

    class GetOutputSerializer(serializers.ModelSerializer):
        specie = PokemonStoragesListingField(read_only=True)

        class Meta:
            model = Storage
            fields = ["id", "nick_name", "is_party_member", "specie"]

    def get(self, request):
        try:
            pokemons_in_party = get_user_party_pokemons(request.user)
            storages_serializer = self.GetOutputSerializer(
                many=True, instance=pokemons_in_party)
            if(len(storages_serializer.data) == 0):
                return Response({"details": "No pokemons have been found in your party"})

            return Response(storages_serializer.data)

        except User.DoesNotExist:
            raise NotFound("User not found")


class SwapPokemonStorage(APIView):
    permission_classes = [IsAuthenticated]

    class InputSerializer(serializers.Serializer):
        entering_the_party = serializers.IntegerField(allow_null=True)
        leaving_the_party = serializers.IntegerField(allow_null=True)

    class GetOutputSerializer(serializers.ModelSerializer):
        specie = PokemonStoragesListingField(read_only=True)

        class Meta:
            model = Storage
            fields = ["id", "nick_name", "is_party_member", "specie"]

    def post(self, request):
        try:
            input_data = self.InputSerializer(data=request.data)
            input_data.is_valid(raise_exception=True)
            validate_both_swap_fields(input_data.data)
            swap_pokemon_party(input_data.data, request.user)

            pokemons_in_party = get_user_party_pokemons(request.user)
            storages_serializer = self.GetOutputSerializer(
                many=True, instance=pokemons_in_party)

            return Response(storages_serializer.data)
        except ValidationError as e:
            raise ValidationError({"detail": e.detail[0]})
        except Storage.DoesNotExist:
            raise ParseError(
                "Please make sure that all the pokemons you entered exist in your storage")
