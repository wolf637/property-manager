from django.shortcuts import render, get_object_or_404, redirect

from .models import Room
from room_types.models import RoomType

# Create your views here.
def list(request):
    rooms = Room.objects
    return render(request, "rooms/list.html", context={'rooms': rooms})



def create(request):

    if request.method == 'POST':
        print(request.POST)
        if request.POST['room_name'] and request.POST['room_type']:
            room = Room()
            room.name = request.POST['room_name']
            room.description = request.POST['room_desc']
            room_type_id = int(request.POST['room_type'])
            room.room_type = get_object_or_404(RoomType, pk=room_type_id)
            room.save()
            return redirect('/rooms/' + str(room.id))
        else:
            return render(request, 'rooms/create.html', {'error': 'All fields are required'})
    else:
        room_types = RoomType.objects
        return render(request, "rooms/create.html", context={'room_types': room_types})








def details(request, room_id):

    room = get_object_or_404(Room, pk=room_id)
    return render(request, "rooms/details.html", context={'room': room})