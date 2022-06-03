import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import pokemons_sprites_stats_data


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating pokemons, sprites and stats...")
            pokemons_sprites_stats_data()
            logging.info("Pokemons, sprites and stats successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
