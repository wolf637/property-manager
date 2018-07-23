from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.models import Property
from .models import Reservation

# Create your views here.

@login_required(login_url='login')
def list(request):

    property = Property.objects.get(user=request.user)
    reservations = {}
    if property:
        reservations = Reservation.objects.filter(property=property)
    return render(request, "reservations/list.html", context={'reservations': reservations})


@login_required(login_url='login')
def create(request):
    return render(request, "reservations/create.html", context={})
@login_required(login_url='login')
def details(request, room_id):
    return render(request, "Here is the list of rooms")