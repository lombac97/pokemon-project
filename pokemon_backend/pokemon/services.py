from rest_framework.exceptions import NotFound, ParseError, ValidationError
from pokemon.models import Storage
from pokemon.serializer import StorageSerializer
from django.db import transaction


def catch_pokemon(data, user_id):
    if(data["is_party_member"]):
        validate_party_full(user_id)

    to_save = StorageSerializer(data={**data, "user": user_id})
    to_save.is_valid(raise_exception=True)
    to_save.save()
    return to_save.data


def get_user_party_pokemons(user_id):
    party_pokemons = Storage.objects.filter(user=user_id, is_party_member=True)
    return party_pokemons


def validate_party_full(user_id):
    party_pokemons = get_user_party_pokemons(user_id)
    if(len(party_pokemons) >= 6):
        raise ParseError("You already have 6 pokemons in your party")


def edit_pokemon(data, user_id, id):
    storage_pokemon = Storage.objects.get(user=user_id, id=id)
    storage_pokemon.nick_name = data["nick_name"]
    storage_pokemon.save()
    return storage_pokemon


def delete_storage_pokemon(id, user_id):
    to_delete = Storage.objects.get(id=id, user=user_id)
    to_delete.delete()


def validate_both_swap_fields(data):
    if(data["entering_the_party"] is None and data["leaving_the_party"] is None):
        raise ValidationError("At least one field should be a number")
    if(data["entering_the_party"] == data["leaving_the_party"]):
        raise ValidationError("You can't swap the same pokemon")


def swap_pokemon_party(data, user):
    pokemon_to_enter = None
    pokemon_to_leave = None
    if(data["entering_the_party"]):
        pokemon_to_enter = enter_pokemon_party(
            data["entering_the_party"], user)
    if(data["leaving_the_party"]):
        pokemon_to_leave = leave_pokemon_party(
            data["leaving_the_party"], user)
    with transaction.atomic():
        if(pokemon_to_enter is not None):
            pokemon_to_enter.save()
        if(pokemon_to_leave is not None):
            pokemon_to_leave.save()


def enter_pokemon_party(pokemon_id, user):
    validate_party_full(user)
    pokemon = Storage.objects.get(id=pokemon_id, user=user)
    if(pokemon.is_party_member):
        raise ValidationError(
            f"{pokemon.nick_name} is already in your party")
    pokemon.is_party_member = True
    return pokemon


def leave_pokemon_party(pokemon_id, user):
    pokemon = Storage.objects.get(id=pokemon_id, user=user)
    if(not(pokemon.is_party_member)):
        raise ParseError(f"{pokemon.nick_name} is not in your party")
    pokemon.is_party_member = False
    return pokemon
