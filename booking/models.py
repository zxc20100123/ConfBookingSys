from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employeeID = models.IntegerField()

    def __str__(self):
        return "{} - {}".format(self.user.id, self.user.username)


class Room(models.Model):
    name = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=True)
    cap = models.IntegerField()
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.name


class RoomBooked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    bookedDate = models.DateField(blank=False)
    bookedHour = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return "{} - {} by {}".format(self.id, self.room.name, self.user.username)
