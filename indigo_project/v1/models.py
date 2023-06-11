from django.db import models


class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    active = models.BooleanField()
 
    def __str__(self) -> str:
        return self.name


class Booking(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    booking_on = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField()
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    price = models.IntegerField()
    active = models.BooleanField()

    def __str__(self) -> str:
        return self.name