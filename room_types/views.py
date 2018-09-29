from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Bed, RoomType


@login_required(login_url='login')
def create(request):
    beds = Bed.objects
    if request.method == 'POST':
        print(request.POST)
        if request.POST['room_type_name'] and request.POST['bed_type']:
            print('ok')


    return render(request, 'room_types/create.html', context={'beds': beds})
