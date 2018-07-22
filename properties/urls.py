from django.urls import path
from . import views

urlpatterns = [

    path('<int:property_id>', views.details, name='property_details'),
]
