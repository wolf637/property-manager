from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Property


def signup(request):

    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['email'])
                return render(request, 'properties/signup.html', context={'error': 'Username already exists'})
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
            return render(request, 'properties/signup.html', context={'error': 'Passwords did not match'})
    else:
        return render(request, 'properties/signup.html', context={})

def login(request):
    return render(request, 'properties/login.html', context={})

def logout(request):
    return render(request, 'properties/signup.html', context={})

def details(request, property_id):

    property = get_object_or_404(Property, pk=property_id)
    return render(request, "properties/property.html", context={'property': property})