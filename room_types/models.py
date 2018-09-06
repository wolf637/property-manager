from django.db import models

# Create your models here.


class Bed(models.Model):

    name = models.TextField(max_length=80)
    occupancy = models.IntegerField()

    def __str__(self):
        return self.name


class RoomType(models.Model):

    name = models.TextField(max_length=80)
    image = models.ImageField(upload_to='images/')
    bed = models.ForeignKey(Bed, on_delete=models.DO_NOTHING)
    num_beds = models.IntegerField(default=1)
    rate = models.IntegerField(default=50)

    def occupancy(self):
        return self.bed.occupancy * self.num_beds

    def __str__(self):
        return self.name
