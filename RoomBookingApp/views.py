from django.shortcuts import render, redirect, get_object_or_404
from .models import Room, Booking
from .forms import RoomForm, BookingForm
from django.db.models import Q
from datetime import date

# Room Views
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'room_create.html', {'form': form})

def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'room_update.html', {'form': form})

def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'room_delete.html', {'room': room})


from datetime import datetime

def is_room_available(room, check_in_date, check_in_time, check_out_date, check_out_time):
    """
    Check if a room is available for the given date and time range.
    """
    # Combine date and time into datetime objects
    check_in_datetime = datetime.combine(check_in_date, check_in_time)
    check_out_datetime = datetime.combine(check_out_date, check_out_time)
    
    # Get all bookings for the specified room
    bookings = Booking.objects.filter(room=room)
    for booking in bookings:
        # Convert existing bookings to datetime objects
        existing_check_in_datetime = datetime.combine(booking.check_in_date, booking.check_in_time)
        existing_check_out_datetime = datetime.combine(booking.check_out_date, booking.check_out_time)
        
        # Check for overlap
        if (check_in_datetime < existing_check_out_datetime and check_out_datetime > existing_check_in_datetime):
            return False
    return True

def check_availability(request):
    if 'check_in_date' in request.GET and 'check_in_time' in request.GET:
        check_in_date_str = request.GET['check_in_date']
        check_in_time_str = request.GET['check_in_time']
        
        # Convert the date and time strings to date and time objects
        check_in_date = datetime.strptime(check_in_date_str, '%Y-%m-%d').date()
        check_in_time = datetime.strptime(check_in_time_str, '%H:%M').time()
        
        # Assuming you need to use the same check-in and check-out date and time for availability
        check_out_date = check_in_date  # If you have different check-out date, update accordingly
        check_out_time = check_in_time  # If you have different check-out time, update accordingly
        
        # Fetch all rooms and filter them based on availability
        rooms = Room.objects.all()
        available_rooms = []
        unavailable_rooms = []

        for room in rooms:
            if is_room_available(room, check_in_date, check_in_time, check_out_date, check_out_time):
                available_rooms.append(room)
            else:
                unavailable_rooms.append(room)
        
        return render(request, 'room_availability_results.html', {
            'available_rooms': available_rooms,
            'unavailable_rooms': unavailable_rooms,
            'check_in_date': check_in_date,
            'check_in_time': check_in_time,
        })
    
    return render(request, 'room_check_availability.html')




# def is_room_available(room, check_in_date, check_in_time, check_out_date, check_out_time):
#     """
#     Check if a room is available for the given date and time range.
#     """
#     # Convert string inputs to date objects
#     check_in_date = datetime.strptime(check_in_date, '%Y-%m-%d').date()
#     check_out_date = datetime.strptime(check_out_date, '%Y-%m-%d').date()
    
#     # Combine date and time into datetime objects
#     check_in_datetime = datetime.combine(check_in_date, check_in_time)
#     check_out_datetime = datetime.combine(check_out_date, check_out_time)
    
#     # Get all bookings for the specified room
#     bookings = Booking.objects.filter(room=room)
#     for booking in bookings:
#         # Convert existing bookings to datetime objects
#         existing_check_in_datetime = datetime.combine(booking.check_in_date, booking.check_in_time)
#         existing_check_out_datetime = datetime.combine(booking.check_out_date, booking.check_out_time)
        
#         # Check for overlap
#         if (check_in_datetime < existing_check_out_datetime and check_out_datetime > existing_check_in_datetime):
#             return False
#     return True

# def check_availability(request):
#     if 'check_in_date' in request.GET and 'check_in_time' in request.GET:
#         check_in_date = request.GET['check_in_date']
#         check_in_time = request.GET['check_in_time']
        
#         # Convert time string to time object
#         check_in_time = datetime.strptime(check_in_time, '%H:%M').time()
        
#         # Fetch all rooms and filter them based on availability
#         rooms = Room.objects.all()
#         available_rooms = []
#         unavailable_rooms = []

#         for room in rooms:
#             if is_room_available(room, check_in_date, check_in_time, check_in_date, check_in_time):
#                 available_rooms.append(room)
#             else:
#                 unavailable_rooms.append(room)
        
#         return render(request, 'room_availability_results.html', {
#             'available_rooms': available_rooms,
#             'unavailable_rooms': unavailable_rooms,
#             'check_in_date': check_in_date,
#             'check_in_time': check_in_time,
#         })
    
#     return render(request, 'room_check_availability.html')



    

# Booking Views
def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'booking_list.html', {'bookings': bookings})

def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            if is_room_available(
                booking.room, 
                booking.check_in_date, 
                booking.check_in_time, 
                booking.check_out_date, 
                booking.check_out_time
            ):
                booking.save()
                return redirect('booking_list')
            else:
                form.add_error(None, "The room is not available for the selected dates and times.")
    else:
        form = BookingForm()
    return render(request, 'booking_create.html', {'form': form})

def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_booking = form.save(commit=False)
            if is_room_available(
                updated_booking.room, 
                updated_booking.check_in_date, 
                updated_booking.check_in_time, 
                updated_booking.check_out_date, 
                updated_booking.check_out_time
            ):
                updated_booking.save()
                return redirect('booking_list')
            else:
                form.add_error(None, "The room is not available for the selected dates and times.")
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_update.html', {'form': form})

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')
    return render(request, 'booking_delete.html', {'booking': booking})

    
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'book_room.html', {'form': form, 'room': room})


# Booking Report View
def booking_report(request):
    bookings = Booking.objects.all()
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)
        bookings = bookings.filter(check_in_date__gte=start_date, check_out_date__lte=end_date)

    return render(request, 'booking_report.html', {
        'bookings': bookings,
        'start_date': start_date,
        'end_date': end_date,
    })


