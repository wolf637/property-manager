from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, "rooms/list.html")



def create(request):
    return render(request, "Here is the list of rooms")


def details(request, room_id):
    return render(request, "Here is the list of rooms")