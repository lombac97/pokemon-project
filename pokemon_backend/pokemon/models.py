from operator import mod
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Move(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        db_table = "moves"


class Ability(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        db_table = "abilities"


class Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        db_table = "types"


class Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_location = models.ForeignKey("Location", models.DO_NOTHING, )
    name = models.CharField(max_length=250)
    pokemon_number = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = "areas"


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_regions = models.ForeignKey("Region", models.DO_NOTHING)
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "locations"


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        db_table = "regions"


class Sprite(models.Model):
    id = models.BigAutoField(primary_key=True)
    front_default = models.CharField(max_length=300,)
    back_default = models.CharField(max_length=300, null=True)
    back_shiny = models.CharField(max_length=300, null=True)
    back_shiny_female = models.CharField(max_length=300, null=True)
    back_female = models.CharField(max_length=300, null=True)
    front_shiny = models.CharField(max_length=300, null=True)
    front_shiny_female = models.CharField(max_length=300,
                                          null=True)
    front_female = models.CharField(max_length=300, null=True)

    class Meta:
        db_table = "sprites"


class Pokemon(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_sprites = models.ForeignKey("Sprite", models.DO_NOTHING)
    name = models.CharField(max_length=150)
    flavor_text = models.CharField(max_length=400)
    capture_rate = models.FloatField()
    weight = models.FloatField()
    height = models.FloatField()

    class Meta:
        db_table = "pokemons"


class Storage(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(User, models.DO_NOTHING)
    id_pokemons = models.ForeignKey("Pokemon", models.DO_NOTHING)
    nick_name = models.CharField(max_length=200)
    party_member = models.BooleanField()

    class Meta:
        db_table = "storages"


class PokemonArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    area_id = models.ForeignKey(Area, models.DO_NOTHING)
    pokemon_id = models.ForeignKey(Pokemon, models.DO_NOTHING)

    class Meta:
        db_table = "pokemons_areas"


class PokemonMove(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon_id = models.ForeignKey(Pokemon, models.DO_NOTHING)
    move_id = models.ForeignKey(Move, models.DO_NOTHING)

    class Meta:
        db_table = "pokemons_moves"


class PokemonType(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon_id = models.ForeignKey(Pokemon, models.DO_NOTHING)
    type_id = models.ForeignKey(Type, models.DO_NOTHING)

    class Meta:
        db_table = "pokemons_types"


class PokemonAbility(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon_id = models.ForeignKey(Pokemon, models.DO_NOTHING)
    ability_id = models.ForeignKey(Ability, models.DO_NOTHING)

    class Meta:
        db_table = "pokemons_abilities"


class Stat(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    value = models.BigIntegerField()
    pokemon_id = models.ForeignKey(Pokemon, models.DO_NOTHING)

    class Meta:
        db_table = "stats"
