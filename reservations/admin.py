from django.contrib import admin
from rooms.models import Room
from room_types.models import RoomType, Bed
from properties.models import Property
from guests.models import Guest
from reservations.models import Reservation

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Bed)
admin.site.register(Property)
admin.site.register(Guest)
admin.site.register(Reservation)