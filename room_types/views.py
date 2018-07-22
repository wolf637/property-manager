from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Bed


@login_required(login_url='login')
def create(request):

    beds = Bed.objects
    return render(request, 'room_types/create.html', context={'beds': beds})
