from django.shortcuts import render
from .models import Bed

def create(request):

    beds = Bed.objects
    return render(request, 'room_types/create.html', context={'beds': beds})
