from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list_guests'),
    path('<int:guest_id>', views.details, name='guest_details'),
]

