from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from properties.models import Property
from django.contrib.auth.models import User
from django.contrib import auth
import datetime
from reservations.models import Reservation

def home(request):
    return render(request, "home.html")

@login_required(login_url='login')
def dashboard(request):

    property = Property.objects.get(user=request.user)
    today = datetime.datetime.today()
    arrivals = Reservation.objects.filter(arrival=today, rooms__property=property)
    departures = Reservation.objects.filter(departure=today, rooms__property=property)
    stayovers = Reservation.objects.filter(arrival__lt=today, departure__gt=today, rooms__property=property)

    return render(request, "dashboard.html", context={'property': property,
                                                      'arrivals': arrivals,
                                                      'departures': departures,
                                                      'stayovers': stayovers})

def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['email'])
                return render(request, 'signup.html', context={'error': 'Username already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['email'],
                                                email=request.POST['email'],
                                                password=request.POST['password1'])
                auth.login(request, user)
                property = Property()
                property.name = request.POST['property_name']
                property.user = request.user
                property.save()

                return redirect('home')

        else:
            return render(request, 'signup.html', context={'error': 'Passwords did not match'})
    else:
        return render(request, 'signup.html', context={})

def login(request):

    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'], password=request.POST['password'])
        if user:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', context={'error': 'Username or password is incorrect'})

    return render(request, 'login.html', context={})

def logout(request):

    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')



