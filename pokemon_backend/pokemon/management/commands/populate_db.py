from django.core.management.base import BaseCommand, CommandError
from pokemon.utils.populate import populate


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        try:
            populate()
        except Exception as e:
            print(e)
            raise CommandError('There was an error')
