from django.shortcuts import render, get_object_or_404

from .models import Room

# Create your views here.
def list(request):
    rooms = Room.objects
    return render(request, "rooms/list.html", context={'rooms': rooms})



def create(request):
    return render(request, "rooms/create.html")


def details(request, room_id):

    room = get_object_or_404(Room, pk=room_id)
    return render(request, "rooms/details.html", context={'room': room})