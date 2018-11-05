from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=80, blank=False)
    picture = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name