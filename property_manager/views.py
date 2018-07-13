from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from properties.models import Property

def home(request):
    return render(request, "home.html")

@login_required(login_url='login.html')
def dashboard(request):

    property = Property.objects.get(user=request.user)
    return render(request, "dashboard.html", context={'property': property})

