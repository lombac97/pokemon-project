import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import abilities_data


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            logging.info("Populating abilities...")
            abilities_data()
            logging.info("Abilities successfully populated")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
