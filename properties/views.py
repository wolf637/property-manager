from django.shortcuts import render, get_object_or_404
from .models import Property


def signup(request):
    return render(request, 'signup.html', context={})

def login(request):
    return render(request, 'login.html', context={})

def logout(request):
    return render(request, 'signup.html', context={})

def details(request, property_id):

    property = get_object_or_404(Property, pk=property_id)
    return render(request, "properties/property.html", context={'property': property})