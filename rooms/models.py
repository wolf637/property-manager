from django.db import models

# Create your models here.

class Room(models.Model):

    name = models.TextField(max_length=80)
    description = models.TextField(max_length=1000)
    image = models.ImageField
    occupancy = models.IntegerField()
    checked_in = models.BooleanField()
    checked_out = models.BooleanField()
    ready = models.BooleanField()
