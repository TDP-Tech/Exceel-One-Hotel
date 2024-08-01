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
]
