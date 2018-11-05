from django.urls import path
from . import views

app_name = 'room_types'

urlpatterns = [
    path('create/', views.create, name='create_room_type'),
    path('<int:room_type_id>', views.details, name='room_type_details'),
]
