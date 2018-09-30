from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name='create_room_type'),
    path('<int:room_type_id>', views.details, name='room_type_details'),
]
