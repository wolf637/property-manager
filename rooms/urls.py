from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='list_rooms'),
    path('create/', views.create, name='create_room'),
    path('<int:room_id>', views.details, name='room_details'),
]
