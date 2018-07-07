from django.contrib import admin
from rooms.models import Room
from room_types.models import RoomType, Bed

# Register your models here.
admin.site.register(Room)
admin.site.register(RoomType)
admin.site.register(Bed)