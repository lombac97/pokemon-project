import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import regions_data


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating regions...")
            regions_data()
            logging.info("Regions successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
