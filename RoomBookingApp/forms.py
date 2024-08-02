from django import forms
from .models import Room, Booking

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'price']
        widgets = {
            'room_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter room number'}),
            'room_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter room type'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter room price'}),
        }
        labels = {
            'room_number': 'Room Number',
            'room_type': 'Room Type',
            'price': 'Room Price',
        }

from django import forms
from django.core.exceptions import ValidationError
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'customer_name', 'check_in_date', 'check_in_time', 'check_out_date', 'check_out_time']
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'check_in_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_in_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'check_out_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_out_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }
        labels = {
            'room': 'Room',
            'customer_name': 'Customer Name',
            'check_in_date': 'Check-In Date',
            'check_in_time': 'Check-In Time',
            'check_out_date': 'Check-Out Date',
            'check_out_time': 'Check-Out Time',
        }

    def clean(self):
        cleaned_data = super().clean()
        check_in_date = cleaned_data.get("check_in_date")
        check_in_time = cleaned_data.get("check_in_time")
        check_out_date = cleaned_data.get("check_out_date")
        check_out_time = cleaned_data.get("check_out_time")
        room = cleaned_data.get("room")

        if check_in_date and check_out_date and check_in_date > check_out_date:
            raise ValidationError("Check-in date cannot be after check-out date.")

        if check_in_date == check_out_date and check_in_time >= check_out_time:
            raise ValidationError("Check-in time cannot be after or the same as check-out time.")

        # Check for overlapping bookings
        if room:
            bookings = Booking.objects.filter(room=room)
            for booking in bookings:
                if (check_in_date <= booking.check_out_date and check_out_date >= booking.check_in_date):
                    if (check_in_time < booking.check_out_time and check_out_time > booking.check_in_time):
                        raise ValidationError("This room is already booked for the selected time.")
