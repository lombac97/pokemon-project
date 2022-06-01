import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import locations_data

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating locations")
            locations_data()
            logging.info("Locations successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
