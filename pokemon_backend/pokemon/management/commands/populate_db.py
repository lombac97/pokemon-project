import logging
from django.core.management.base import BaseCommand, CommandError
from pokemon.management.commands.populate_abilities import Command as PopulateAbilities
from pokemon.management.commands.populate_areas import Command as PopulateAreas
from pokemon.management.commands.populate_locations import Command as PopulateLocations
from pokemon.management.commands.populate_moves import Command as PopulateMoves
from pokemon.management.commands.populate_pokemon_areas import Command as PopulatePokemonAreas
from pokemon.management.commands.populate_pokemon_types_abilities import Command as PopulatePokemonTypesAbilities
from pokemon.management.commands.populate_pokemons import Command as PopulatePokemons
from pokemon.management.commands.populate_regions import Command as PopulateRegions
from pokemon.management.commands.populate_types import Command as PopulateTypes


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        instances = [PopulateRegions(), PopulateLocations(), PopulateAreas(), PopulateMoves(), PopulateTypes(
        ), PopulateAbilities(), PopulatePokemons(), PopulatePokemonAreas(), PopulatePokemonTypesAbilities()]
        try:
            logging.info("Populating the database...")
            for elem in instances:
                elem.handle()
            logging.info("The database has been populated successfully")
        except Exception as e:
            logging.error(e)
            raise CommandError('There was an error')
