from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Room(models.Model):
    room_number = models.CharField(max_length=50, unique=True)
    room_type = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rooms')

    def __str__(self):
        return self.room_number

from django.core.exceptions import ValidationError
from django.db import models
from datetime import datetime

class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked-In'),
        ('checked_out', 'Checked-Out'),
        ('canceled', 'Canceled'),
    ]
    
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    check_in_date = models.DateField()
    check_in_time = models.TimeField()
    check_out_date = models.DateField()
    check_out_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Booking for {self.customer_name} in room {self.room}"

    def clean(self):
        # Check if check-in date is before check-out date
        if self.check_in_date > self.check_out_date:
            raise ValidationError("Check-in date cannot be after check-out date.")
        
        if self.check_in_date == self.check_out_date and self.check_in_time >= self.check_out_time:
            raise ValidationError("Check-in time cannot be after or the same as check-out time.")

        # Check for overlapping bookings
        bookings = Booking.objects.filter(room=self.room)
        for booking in bookings:
            if (self.check_in_date <= booking.check_out_date and self.check_out_date >= booking.check_in_date):
                if (self.check_in_time < booking.check_out_time and self.check_out_time > booking.check_in_time):
                    raise ValidationError("This room is already booked for the selected time.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
