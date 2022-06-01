import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import pokemon_moves_types_abilities


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating Pokemon, Moves, Types and Abilities relations")
            pokemon_moves_types_abilities()
            logging.info("Pokemon, Moves, Types and Abilities relations successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
