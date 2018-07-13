from django.db import models
from guests.models import Guest
from rooms.models import Room
from room_types.models import RoomType
from properties.models import Property

# Create your models here.

class Reservation(models.Model):


    arrival = models.DateField()
    departure = models.DateField()
    guest = models.ForeignKey(Guest, on_delete=models.DO_NOTHING)
    room_types = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING)
    rooms = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
