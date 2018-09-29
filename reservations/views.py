from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from properties.models import Property
from rooms.models import Room
from .models import Reservation
from guests.models import Guest
import datetime

# Create your views here.

@login_required(login_url='login')
def list(request):

    property = Property.objects.get(user=request.user)
    reservations = Reservation.objects.filter(rooms__property=property)
    return render(request, "reservations/list.html", context={'reservations': reservations})


@login_required(login_url='login')
def create(request):

    if request.method == 'POST':
        if (request.POST['first_name']
            and request.POST['last_name']
            and request.POST['arrival']
            and request.POST['departure']
            and request.POST['email']
            and request.POST['phone']):

            arrival =  datetime.datetime.strptime(request.POST['arrival'], "%m/%d/%Y").date()
            departure = datetime.datetime.strptime(request.POST['departure'], "%m/%d/%Y").date()


            guest, created = Guest.objects.get_or_create(first_name=request.POST['first_name'],
                                                         last_name=request.POST['last_name'],
                                                         email=request.POST['email'],
                                                         phone=request.POST['phone'])

            rooms = Room.objects.get(id=request.POST['rooms'])

            reservation = Reservation(guest=guest,
                                      arrival=arrival,
                                      departure=departure,
                                      rooms=rooms)

            reservation.save()
            return redirect('/reservations/' + str(reservation.id))
        else:
            return render(request, 'reservations/create.html', {'error': 'All fields are required'})

    property = Property.objects.get(user=request.user)
    rooms = Room.objects.filter(property=property)
    return render(request, "reservations/create.html", context={'rooms': rooms})

@login_required(login_url='login')
def details(request, reservation_id):

    reservation = Reservation.objects.get(id=reservation_id)
    return render(request, "reservations/details.html", context={'reservation': reservation})