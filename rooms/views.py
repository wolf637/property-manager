from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Room
from room_types.models import RoomType
from properties.models import Property

@login_required(login_url='login')
def list(request):

    # TODO In some cases when I an logged in as an admin I don't have property or rooms associated so it causes properties.models.DoesNotExist: Property matching query does not exist.


    property = Property.objects.get(user=request.user)
    rooms = {}
    if property:
        rooms = Room.objects.filter(property=property)
    return render(request, "rooms/list.html", context={'rooms': rooms})


@login_required(login_url='login')
def create(request):

    if request.method == 'POST':
        if request.POST['room_name'] and request.POST['room_type']:
            room = Room()
            room.name = request.POST['room_name']
            room.property = get_object_or_404(Property, request.user.id)
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


@login_required(login_url='login')
def details(request, room_id):
    property = Property.objects.get(user=request.user)
    room = get_object_or_404(Room, pk=room_id, property=property)
    return render(request, "rooms/details.html", context={'room': room})