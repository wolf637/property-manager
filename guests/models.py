from django.db import models

# Create your models here.

class Guest(models.Model):

    first_name = models.TextField(max_length=80)
    last_name = models.TextField(max_length=80)
    email = models.EmailField()
    phone = models.TextField()

