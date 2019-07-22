from django.db import models
from uuid import uuid4
# Create your models here.

class Areas(models.Model):
    areaId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    pokeballs = models.CharField(max_length=99999, blank=True, null=True)
    pokemon = models.CharField(max_length=99999, blank=True, null=True)
    coords = models.TextField(blank=True, null=True)
    exits = models.TextField(blank=True, null=True)
    players = models.TextField(blank=True, null=True)

class Users(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    password = models.CharField(max_length=248, unique=False, blank=True, null=True)
    items = models.CharField(max_length=64, blank=True, null=True)
    area_id = models.CharField(max_length=128, blank=True, null=True)
    pokemon = models.CharField(max_length=99999, blank=True, null=True)
    pokeballs = models.CharField(max_length=99999, blank=True, null=True)

class Pokemon(models.Model):
    pokemonId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True, blank=True, null=True)
    catchChance = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    spawnChance = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)

class Pokeballs(models.Model):
    pokeballId = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True, blank=True, null=True)
    catchRate = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
    spawnChance = models.DecimalField(max_digits=5, decimal_places=4, blank=True, null=True)
