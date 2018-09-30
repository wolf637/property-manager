from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from properties.models import Property
from .models import Guest

@login_required(login_url='login')
def list(request):

    property = Property.objects.get(user=request.user)
    guests = Guest.objects.get(property=property)
    return render(request, "rooms/list.html", context={'guests': guests})
