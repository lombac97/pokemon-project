from rest_framework import serializers
from .models import Pokemon, Sprite


class SpriteOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprite
        fields = ["front_default",
                  "back_default",
                  "back_shiny",
                  "back_shiny_female",
                  "back_female",
                  "front_shiny",
                  "front_shiny_female",
                  "front_female"]


class PokemonFromAreaOutputSerializer(serializers.ModelSerializer):
    sprites = SpriteOutputSerializer()

    class Meta:
        model = Pokemon
        fields = ["id", "name", "sprites"]
