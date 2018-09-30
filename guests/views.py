from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.models import Property
from .models import Guest

@login_required(login_url='login')
def list(request):

    property = Property.objects.get(user=request.user)
    guests = Guest.objects.filter(property=property)
    return render(request, "guests/list.html", context={'guests': guests})


@login_required(login_url='login')
def details(request, guest_id):

    guest = Guest.objects.get(id=guest_id)
    return render(request, "guests/details.html", context={'guest': guest})