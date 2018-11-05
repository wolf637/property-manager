from django.db import models
from room_types.models import RoomType
from properties.models import Property

# Create your models here.

class Room(models.Model):

    name = models.TextField(max_length=80)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, blank=True)
    description = models.TextField(max_length=1000, default="")
    room_type = models.ForeignKey(RoomType, on_delete=models.DO_NOTHING, blank=False)
    empty = models.BooleanField(default=True)
    ready = models.BooleanField(default=True)

    def occupancy(self):
        return self.room_type.occupancy()

    def image(self):
        return self.room_type.image

    def __str__(self):
        return self.name
