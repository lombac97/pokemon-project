import json

from pokemon.models import Ability, Area, Location, Move, Pokemon, PokemonArea, Region, Type
from pokemon.serializer import AbilitySerializer, AreaSerializer, LocationSerializer, MoveSerializer, PokemonAbilitySerializer, PokemonAreaSerializer, PokemonMoveSerializer, PokemonSerializer, PokemonTypeSerializer, RegionSerializer, SpriteSerializer, StatSerializer, TypeSerializer


def regions_data():
    file = open("pokemon/utils/jsons/regions.json")
    data = json.load(file)
    dict_list = []
    for region in data["data"]:
        dict_list.append({"name": region["name"]})

    region_serializer = RegionSerializer(
        many=True, data=dict_list)

    region_serializer.is_valid(raise_exception=True)
    region_serializer.save()
    file.close()


def locations_data():
    file = open("pokemon/utils/jsons/regions.json")
    data = json.load(file)
    dict_list = []
    for region in data["data"]:
        region_id = Region.objects.get(name=region["name"])

        for location in region["locations"]:
            dict_list.append({"name": location, "regions": region_id.id})
    location_serializer = LocationSerializer(many=True, data=dict_list)
    location_serializer.is_valid(raise_exception=True)
    location_serializer.save()

    file.close()


def areas_data():
    file = open("pokemon/utils/jsons/areas.json")
    data = json.load(file)
    dict_list = []
    for area in data["data"]:
        location_id = Location.objects.get(name=area["location"])

        dict_list.append(
            {"name": area["name"], "location": location_id.id, "pokemon_count": len(area["pokemons"])})
    area_serializer = AreaSerializer(many=True, data=dict_list)
    area_serializer.is_valid(raise_exception=True)
    area_serializer.save()
    file.close()


def moves_data():
    file = open("pokemon/utils/jsons/pokemons.json")
    data = json.load(file)
    dict_list = []
    moves_dict = {}
    for pokemon in data["data"]:
        for move in pokemon["moves"]:
            if(not move in moves_dict):
                dict_list.append({"name": move})
                moves_dict[move] = 1
    moves_serializer = MoveSerializer(many=True, data=dict_list)
    moves_serializer.is_valid(raise_exception=True)
    moves_serializer.save()
    file.close()


def types_data():
    file = open("pokemon/utils/jsons/pokemons.json")
    data = json.load(file)
    dict_list = []
    types_dict = {}
    for pokemon in data["data"]:
        for type in pokemon["types"]:
            if(not type in types_dict):
                dict_list.append({"name": type})
                types_dict[type] = 1
    types_serializer = TypeSerializer(many=True, data=dict_list)
    types_serializer.is_valid(raise_exception=True)
    types_serializer.save()
    file.close()


def abilities_data():
    file = open("pokemon/utils/jsons/pokemons.json")
    data = json.load(file)
    dict_list = []
    abilities_dict = {}
    for pokemon in data["data"]:
        for ability in pokemon["abilities"]:
            if(not ability in abilities_dict):
                dict_list.append({"name": ability})
                abilities_dict[ability] = 1
    abilities_serializer = AbilitySerializer(many=True, data=dict_list)
    abilities_serializer.is_valid(raise_exception=True)
    abilities_serializer.save()
    file.close()


def pokemons_sprites_stats_data():
    file = open("pokemon/utils/jsons/pokemons.json")
    data = json.load(file)
    stats_list = []
    for pokemon in data["data"]:
        sprite = pokemon["sprites"]

        sprite_serializer = SpriteSerializer(data=sprite)
        sprite_serializer.is_valid(raise_exception=True)
        saved_sprite = sprite_serializer.save()

        pokemon_serializer = PokemonSerializer(
            data={**pokemon, "sprite": saved_sprite.id})

        pokemon_serializer.is_valid(raise_exception=True)
        saved_pokemon = pokemon_serializer.save()
        for stat in pokemon["stats"]:
            stats_list.append({**stat, "pokemon": saved_pokemon.id})
    stats_serializer = StatSerializer(many=True, data=stats_list)
    stats_serializer.is_valid(raise_exception=True)
    stats_serializer.save()
    file.close()


def pokemon_areas():

    file = open("pokemon/utils/jsons/areas.json")
    data = json.load(file)
    dict_list = []
    for area in data["data"]:

        area_db = Area.objects.get(name=area["name"])
        pokemons_in_area = map(lambda x: x.capitalize(), area["pokemons"])
        pokemon_db = Pokemon.objects.filter(name__in=pokemons_in_area)
        for elem in pokemon_db:
            dict_list.append({"pokemon": elem.id, "area": area_db.id})

    pokemon_area_serializer = PokemonAreaSerializer(many=True, data=dict_list)
    pokemon_area_serializer.is_valid(raise_exception=True)
    pokemon_area_serializer.save()
    file.close()


def pokemon_moves_types_abilities():
    file = open("pokemon/utils/jsons/pokemons.json")
    data = json.load(file)
    dict_list_moves = []
    dict_list_types = []
    dict_list_abilities = []
    for pokemon in data["data"]:

        pokemon_db = Pokemon.objects.get(name=pokemon["name"])
        moves = Move.objects.filter(name__in=pokemon["moves"])
        abilities = Ability.objects.filter(name__in=pokemon["abilities"])
        types = Type.objects.filter(name__in=pokemon["types"])

        for elem in moves:
            dict_list_moves.append({"move": elem.id, "pokemon": pokemon_db.id})
        for elem in abilities:
            dict_list_abilities.append(
                {"ability": elem.id, "pokemon": pokemon_db.id})
        for elem in types:
            dict_list_types.append({"type": elem.id, "pokemon": pokemon_db.id})

    pokemon_moves_serializer = PokemonMoveSerializer(
        many=True, data=dict_list_moves)
    pokemon_abilities_serializer = PokemonAbilitySerializer(
        many=True, data=dict_list_abilities)
    pokemon_types_serializer = PokemonTypeSerializer(
        many=True, data=dict_list_types)

    pokemon_moves_serializer.is_valid(raise_exception=True)
    pokemon_abilities_serializer.is_valid(raise_exception=True)
    pokemon_types_serializer.is_valid(raise_exception=True)

    pokemon_moves_serializer.save()
    pokemon_abilities_serializer.save()
    pokemon_types_serializer.save()

    file.close()
