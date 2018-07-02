from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, "reservations/list.html")



def create(request):
    return render(request, "Here is the list of rooms")


def details(request, room_id):
    return render(request, "Here is the list of rooms")