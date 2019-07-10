from django.db import models
from uuid import uuid4
# Create your models here.

class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    items = models.TextField(blank=True)
