import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import pokemon_areas


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating pokemon areas")
            pokemon_areas()
            logging.info("Pokemon areas successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
