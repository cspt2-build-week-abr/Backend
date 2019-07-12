from django.db import models
from uuid import uuid4
# Create your models here.

class Areas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=64, blank=True)
    pokeballs = models.CharField(max_length=128, blank=True)
    pokemon = models.CharField(max_length=128, blank=True)
    adjacents = models.CharField(max_length=4, blank=True)
    players = models.Textfield(blank=True)

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True, blank=True)
    token = models.CharField(max_length=248, unique=True, blank=True)
    items = models.CharField(max_length=64, blank=True)
    area_id = models.IntegerField()

class Pokemon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True, blank=True)
    catchChance = models.DecimalField(max_digits=3, decimal_places=2, blank=True)
    spawnChance = models.DecimalField(max_digits=3, decimal_places=2, blank=True)

class Pokeballs(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=64, unique=True, blank=True)
    catchRate = models.DecimalField(max_digits=4, decimal_places=4, blank=True)
