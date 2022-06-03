from django.db import models

# Create your models here.


class Region(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)

    class Meta:
        db_table = "regions"


# Create your models here.


class Location(models.Model):
    id = models.BigAutoField(primary_key=True)
    region = models.ForeignKey(
        Region, models.DO_NOTHING, related_name="locations")
    name = models.CharField(max_length=200)

    class Meta:
        db_table = "locations"


class Area(models.Model):
    id = models.BigAutoField(primary_key=True)
    location = models.ForeignKey(
        "Location", models.DO_NOTHING, related_name="areas")
    name = models.CharField(max_length=250, unique=True)
    pokemon_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = "areas"
