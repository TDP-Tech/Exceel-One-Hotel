from django.contrib import admin
from .models import Room, Booking

class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price', 'user')
    list_filter = ('room_type',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('room', 'customer_name', 'check_in_date', 'check_out_date')
    list_filter = ('check_in_date', 'check_out_date')

admin.site.register(Room, RoomAdmin)
admin.site.register(Booking, BookingAdmin)
