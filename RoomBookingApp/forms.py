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

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'customer_name', 'check_in_date', 'check_out_date']
        widgets = {
            'room': forms.Select(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter customer name'}),
            'check_in_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'room': 'Room',
            'customer_name': 'Customer Name',
            'check_in_date': 'Check-In Date',
            'check_out_date': 'Check-Out Date',
        }
