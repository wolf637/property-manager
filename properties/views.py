from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Property



@login_required(login_url='login')
def details(request, property_id):

    property = get_object_or_404(Property, pk=property_id)
    return render(request, "properties/property.html", context={'property': property})