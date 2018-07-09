from django.contrib import admin
from rooms.models import Room
from room_types.models import RoomType, Bed
from properties.models import Property

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Bed)
admin.site.register(Property)