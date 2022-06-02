from django.db import models
from django.contrib.auth.models import User

from places.models import Area
# Create your models here.


class Move(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        db_table = "moves"


class Ability(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)

    class Meta:
        db_table = "abilities"


class Type(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        db_table = "types"


class Sprite(models.Model):
    id = models.BigAutoField(primary_key=True)
    front_default = models.CharField(max_length=300, null=True)
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
    sprite = models.ForeignKey("Sprite", models.DO_NOTHING)
    name = models.CharField(max_length=150)
    flavor_text = models.CharField(max_length=400)
    capture_rate = models.FloatField()
    weight = models.FloatField()
    height = models.FloatField()
    color = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = "pokemons"


class Storage(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING)
    specie = models.ForeignKey("Pokemon", models.DO_NOTHING)
    nick_name = models.CharField(max_length=200)
    is_party_member = models.BooleanField()
    
    class Meta:
        db_table = "storages"


class PokemonArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, related_name="pokemons")
    pokemon = models.ForeignKey(
        Pokemon, models.DO_NOTHING)

    class Meta:
        db_table = "pokemons_areas"


class PokemonMove(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon = models.ForeignKey(
        Pokemon, models.DO_NOTHING, related_name="moves")
    move = models.ForeignKey(Move, models.DO_NOTHING)

    class Meta:
        db_table = "pokemons_moves"


class PokemonType(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon = models.ForeignKey(
        Pokemon, models.DO_NOTHING, related_name='types')
    type = models.ForeignKey(Type, models.DO_NOTHING)

    class Meta:
        db_table = "pokemons_types"


class PokemonAbility(models.Model):
    id = models.BigAutoField(primary_key=True)
    pokemon = models.ForeignKey(
        Pokemon, models.DO_NOTHING, related_name='abilities')
    ability = models.ForeignKey(Ability, models.DO_NOTHING)

    class Meta:
        db_table = "pokemons_abilities"


class Stat(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250)
    value = models.BigIntegerField()
    pokemon = models.ForeignKey(
        Pokemon, models.DO_NOTHING, related_name="stats")

    class Meta:
        db_table = "stats"
