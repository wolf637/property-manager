from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Bed, RoomType
from rooms.models import Room
from properties.models import Property


@login_required(login_url='login')
def create(request):

    beds = Bed.objects
    if request.method == 'POST':
        if request.POST['room_type_name'] \
                and request.POST['bed_type'] \
                and request.POST['num_beds'] \
                and request.POST['rate'] \
                and request.FILES['room_img']:

            bed = Bed.objects.get(id=request.POST['bed_type'])
            name = request.POST['room_type_name']
            num_beds = request.POST['num_beds']
            rate = request.POST['rate']
            image = request.FILES['room_img']

            room_type = RoomType(name=name,
                                 bed=bed,
                                 num_beds=num_beds,
                                 rate=rate,
                                 image=image)
            room_type.save()
            return redirect('/room_types/' + str(room_type.id))
        else:
            return render(request, 'room_types/create.html', {'error': 'All fields are required'})

    return render(request, 'room_types/create.html', {'beds': beds})


@login_required(login_url='login')
def details(request, room_type_id):

    type = get_object_or_404(RoomType, pk=room_type_id)
    return render(request, "room_types/details.html", context={'type': type})

