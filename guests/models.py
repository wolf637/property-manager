from django.db import models
from properties.models import Property

# Create your models here.

class Guest(models.Model):

    first_name = models.TextField(max_length=80)
    last_name = models.TextField(max_length=80)
    email = models.EmailField()
    phone = models.TextField()
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING, default=1)


    def __str__(self):
        return "{last_name}, {first_name}".format(last_name=self.last_name, first_name=self.first_name)

