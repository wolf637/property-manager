from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('<int:property_id>', views.details, name='property_details'),
]
