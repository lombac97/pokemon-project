import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import moves_data


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating moves...")
            moves_data()
            logging.info("Moves successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
