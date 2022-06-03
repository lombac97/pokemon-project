import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import types_data


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating types...")
            types_data()
            logging.info("Types successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
