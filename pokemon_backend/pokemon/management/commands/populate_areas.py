import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import areas_data


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating areas...")
            areas_data()
            logging.info("Areas successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
