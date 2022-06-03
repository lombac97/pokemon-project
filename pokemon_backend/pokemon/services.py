from rest_framework.exceptions import ParseError, ValidationError
from pokemon.models import Storage
from pokemon.serializer import StorageSerializer
from django.db import transaction


def catch_pokemon(data, user_id):
    """
    Catches a new pokemon

    Parameters
    ----------
    user_id: Authenticated user from Token
    data that contains:
        - nick_name: The pokemon nick_name
        - specie: The pokemon id
        - is_party_member: defines wether to include the pokemon in your party

    """

    if(data["is_party_member"]):
        validate_party_full(user_id)

    to_save = StorageSerializer(data={**data, "user": user_id})
    to_save.is_valid(raise_exception=True)
    to_save.save()
    return to_save.data


def get_user_party_pokemons(user_id):
    """
    Get all the pokemons in the party of a user

    Parameters
    ----------
    user_id: Authenticated user from Token

    """

    party_pokemons = Storage.objects.filter(user=user_id, is_party_member=True)
    return party_pokemons


def validate_party_full(user_id):
    """
    Validates if the party is already full (has 6 pokemons)

    Parameters
    ----------
    user_id: Authenticated user from Token

    """

    party_pokemons = get_user_party_pokemons(user_id)
    if(len(party_pokemons) >= 6):
        raise ParseError("You already have 6 pokemons in your party")


def validate_party_full_and_excluding(user_id, leaving_the_party):
    """
    Validates if the party is already full (has 6 pokemons) and the user is excluding a pokemon

    Parameters
    ----------
    user_id: Authenticated user from Token
    leaving_the_party: Defines wether the user is excluding a Pokemon from the party

    """

    party_pokemons = get_user_party_pokemons(user_id)
    if(len(party_pokemons) >= 6 and leaving_the_party is None):
        raise ParseError("You already have 6 pokemons in your party")


def edit_pokemon(data, user_id, id):
    """
    Parameters
    ----------
    user_id: Authenticated user from Token
    data that contains:
        - nick_name: new nick_name for the pokemon
    id: id of the pokemon in your storage to edit
    """

    storage_pokemon = Storage.objects.get(user=user_id, id=id)
    storage_pokemon.nick_name = data["nick_name"]
    storage_pokemon.save()
    return storage_pokemon


def delete_storage_pokemon(id, user_id):
    """
    Parameters
    ----------
    user_id: Authenticated user from Token
    id: id of the pokemon in your storage to delete
    """

    to_delete = Storage.objects.get(id=id, user=user_id)
    to_delete.delete()


def validate_both_swap_fields(data):
    """
    Checks if at least one of the necessary fields exist.
    Also checks if both fields are not the same

    Parameters
    ----------
    data that contains:
        - entering_the_party: pokemon storage id to enter the party
        - leaving_the_party: pokemon storage id to leave the party

    """

    if(data["entering_the_party"] is None and data["leaving_the_party"] is None):
        raise ValidationError("At least one field should be a number")
    if(data["entering_the_party"] == data["leaving_the_party"]):
        raise ValidationError({"You can't swap the same pokemon"})


def swap_pokemon_party(data, user):
    """
    Does an atomic transaction to include and exclude pokemons from the party

    Parameters
    ----------
    user_id: Authenticated user from Token
    data that contains:
        - entering_the_party: pokemon storage id to enter the party
        - leaving_the_party: pokemon storage id to leave the party
    """

    with transaction.atomic():
        if(data["leaving_the_party"]):
            leave_pokemon_party(
                data["leaving_the_party"], user)
        if(data["entering_the_party"]):
            enter_pokemon_party(
                data["entering_the_party"], user, data["leaving_the_party"])


def enter_pokemon_party(pokemon_id, user, leaving_the_party):
    """
    Includes a new pokemon to the party

    Parameters
    ----------
    user_id: Authenticated user from Token
    pokemon_id: Pokemon to include in the party
    leaving_the_party: defines wether the user also excluded a pokemon
    Raises
    ------
    ValidationError
        If the pokemon is already in the party
    Storage.DoesNotExist
        If the pokemon does not exist in the user storage
    """

    validate_party_full_and_excluding(user, leaving_the_party)
    pokemon = Storage.objects.get(id=pokemon_id, user=user)
    if(pokemon.is_party_member):
        raise ValidationError(
            f"{pokemon.nick_name} is already in your party")
    pokemon.is_party_member = True
    pokemon.save()


def leave_pokemon_party(pokemon_id, user):
    """
    Excludes a pokemon out the party

    Parameters
    ----------
    user_id: Authenticated user from Token
    pokemon_id: Pokemon to include in the party

    Raises
    ------
    ValidationError
        If the pokemon is not already in the party
    Storage.DoesNotExist
        If the pokemon does not exist in the user storage
    """

    pokemon = Storage.objects.get(id=pokemon_id, user=user)
    if(not(pokemon.is_party_member)):
        raise ParseError(f"{pokemon.nick_name} is not in your party")
    pokemon.is_party_member = False
    pokemon.save()
