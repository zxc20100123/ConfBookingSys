from django.contrib import admin
from .models import Employee, Room, RoomBooked

# Register your models here.
admin.site.register(Employee)
admin.site.register(Room)
admin.site.register(RoomBooked)