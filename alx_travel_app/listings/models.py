from django.db import models


# Create your models here.

class Bookings(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    room_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Booking {self.booking_id} by User {self.user_id} for Room {self.room_id}"
