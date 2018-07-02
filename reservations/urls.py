from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list_reservations'),
    path('create/', views.create, name='create_reservation'),
    path('<int:reservation_id>', views.details, name='reservation_details'),
]
