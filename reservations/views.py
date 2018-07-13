from django.shortcuts import render
from properties.models import Property
from .models import Reservation

# Create your views here.
def list(request):

    property = Property.objects.get(user=request.user)
    reservations = Reservation.objects.filter(property=property)

    return render(request, "reservations/list.html", context={'reservations': reservations})



def create(request):
    return render(request, "reservations/create.html", context={})


def details(request, room_id):
    return render(request, "Here is the list of rooms")