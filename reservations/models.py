from django.db import models
from guests.models import Guest
from rooms.models import Room

# Create your models here.

class Reservation(models.Model):


    arrival = models.DateField()
    departure = models.DateField()
    guest = models.ForeignKey(Guest, on_delete=models.DO_NOTHING)
    rooms = models.ForeignKey(Room, on_delete=models.DO_NOTHING, blank=True)


    def __str__(self):
        return str(self.pk)
