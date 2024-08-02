from django.urls import path
from . import views

urlpatterns = [
    # Room URLs
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/create/', views.room_create, name='room_create'),
    path('rooms/update/<int:pk>/', views.room_update, name='room_update'),
    path('rooms/delete/<int:pk>/', views.room_delete, name='room_delete'),

    # Booking URLs
    path('bookings/', views.booking_list, name='booking_list'),
    path('bookings/create/', views.booking_create, name='booking_create'),
    path('bookings/update/<int:pk>/', views.booking_update, name='booking_update'),
    path('bookings/delete/<int:pk>/', views.booking_delete, name='booking_delete'),
    
    #book available rooms
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path('booking-report/', views.booking_report, name='booking_report'),
    path('check-availability/', views.check_availability, name='check_availability'),
    
    
]
