from django.db import models


class Hotel_Details(models.Model):
    hotel_name = models.CharField(max_length=50)
    hotel_location = models.TextField()
    room_price = models.IntegerField(default=True)
    max_rooms = models.IntegerField(default=True)
    before_days=models.IntegerField(default=True)
    min_slot=models.IntegerField(default=True)


class Manager_profile(models.Model):
    username=models.CharField(max_length=100)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)


class Time_slots(models.Model):
    pass
