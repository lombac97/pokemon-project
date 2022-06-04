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
    """
    Lists attributes and all info of a pokemon

    Methods
    -------
    get(request, pk)
        Lists all the information about a pokemon

    """
    class OutputSerializer(serializers.ModelSerializer):
        abilities = AbilitiesListingField(many=True, read_only=True)
        types = TypesListingField(many=True, read_only=True)
        moves = MovesListingField(many=True, read_only=True)
        stats = StatsListingField(many=True, read_only=True)
        sprites = SpriteOutputSerializer()

        class Meta:
            model = Pokemon
            fields = "__all__"

    def get(self, request, pk):
        """
        Parameters
        ----------
        pk: Pokemon id in database

        Raises
        ------
        Pokemon.DoesNotExist
            If pokemon does not exist in the database
        """
        try:
            pokemon = Pokemon.objects.get(pk=pk)
            pokemon_serializer = self.OutputSerializer(instance=pokemon)
            return Response(pokemon_serializer.data)
        except Pokemon.DoesNotExist:
            raise NotFound("Pokemon not found")


class OwnPokemonInfo(APIView):
    """
    Lists pokemon in your storage, edits nick_name and deletes pokemon from your storage

    Methods
    -------
    get(request)
        Lists all the pokemons in the user storage

    post(request)
        Catches a new pokemon

    put(request, pk), patch(request, pk)
        Edits a pokemon nick_name

    delete(request, pk)
        Deletes a pokemon from your storage
    """

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
        """
        Parameters
        ----------
        request.user: Authenticated user from Token

        Raises
        ------
        User.DoesNotExist
            If the user does not exist in the database
        """

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
        """
        Parameters
        ----------
        request.user: Authenticated user from Token
        request.data that contains:
            - nick_name: Nick_name for the new catched pokemon
            - specie: id of the new catched pokemon
            - is_party_member: defines wether to include the pokemon in your party

        Raises
        ------
        ValidationError
            If the JSON sent is invalid
        """

        try:
            input_data = self.InputSerializer(data=request.data)
            input_data.is_valid(raise_exception=True)
            save_data = catch_pokemon(input_data.data, request.user.id)
            save_data.pop("user")
            return Response(save_data, HTTPStatus.CREATED)
        except ValidationError:
            raise ParseError("Invalid data")

    def put(self, request, pk):
        """
        Parameters
        ----------
        request.user: Authenticated user from Token
        request.data that contains:
            - nick_name: new nick_name for the pokemon
            - pk: id of the pokemon in your storage to edit

        Raises
        ------
        ValidationError 
            If the JSON sent is invalid
        Storage.DoesNotExist
            If the Pokemon does not exist in your storage
        """
        return self.edit_nick_name(request, pk)

    def patch(self, request, pk):
        """
        Parameters
        ----------
        request.user: Authenticated user from Token
        request.data that contains:
            - nick_name: new nick_name for the pokemon
            - pk: id of the pokemon in your storage to edit

        Raises
        ------
        ValidationError 
            If the JSON sent is invalid
        Storage.DoesNotExist
            If the Pokemon does not exist in your storage
        """
        return self.edit_nick_name(request, pk)

    def edit_nick_name(self, request, pk):
        """
        Parameters
        ----------
        request.user: Authenticated user from Token
        request.data that contains:
            - nick_name: new nick_name for the pokemon
            - pk: id of the pokemon in your storage to edit

        Raises
        ------
        ValidationError 
            If the JSON sent is invalid
        Storage.DoesNotExist
            If the Pokemon does not exist in your storage
        """
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
        """
        Parameters
        ----------
        request.user: Authenticated user from Token
        request.data that contains:
            - pk: id of the pokemon in your storage to delete

        Raises
        ------
        ValidationError 
            If the JSON sent is invalid
        Storage.DoesNotExist
            If the Pokemon does not exist in your storage
        """
        try:
            delete_storage_pokemon(pk, request.user.id)
            return Response(None, HTTPStatus.NO_CONTENT)
        except ValidationError:
            raise ParseError("Invalid data")
        except Storage.DoesNotExist:
            raise NotFound("Pokemon not found")


class OwnPokemonPartyInfo(APIView):
    """
    Lists all the pokemons in your party

    Methods
    -------
    get(request, pk)
        Lists all the pokemons in your party

    """

    permission_classes = [IsAuthenticated]

    class GetOutputSerializer(serializers.ModelSerializer):
        specie = PokemonStoragesListingField(read_only=True)

        class Meta:
            model = Storage
            fields = ["id", "nick_name", "is_party_member", "specie"]

    def get(self, request):
        """
        Parameters
        ----------
        request.user: Authenticated user from Token

        Raises
        ------

        User.DoesNotExist
            If the user does not exist in the database
        """

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
    """
    Includes or exclude (or both) pokemons from your party

    Methods
    -------
    post(request, pk)
        Swaps pokemon in your party

    """

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
        """
        Parameters
        ----------
        request.user: Authenticated user from Token
        request.data that contains:
            - entering_the_party: storage id of the pokemon entering the party
            - leaving_the_party: storage id of the pokemon leaving the party

        Raises
        ------

        ValidationError 
            If the JSON sent is invalid or the operation is invalid
        Storage.DoesNotExist
            If the Pokemon does not exist in your storage
        """

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
            raise ValidationError({"detail": e.detail})
        except Storage.DoesNotExist:
            raise ParseError(
                "Please make sure that all the pokemons you entered exist in your storage")
