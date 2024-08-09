from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Drink, Order
from RoomBookingApp.models import Booking
from .forms import FoodForm, DrinkForm, OrderForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Food Views
@login_required
def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')  # Replace with your actual URL name
    else:
        form = FoodForm()
    return render(request, 'food_create.html', {'form': form})

@login_required
def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

@login_required
def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'food_update.html', {'form': form})

@login_required
def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('food_list')
    return render(request, 'food_delete.html', {'food': food})

# Drink Views
@login_required
def drink_create(request):
    if request.method == 'POST':
        form = DrinkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('drink_list')  # Replace with your actual URL name
    else:
        form = DrinkForm()
    return render(request, 'drink_create.html', {'form': form})

@login_required
def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drink_list.html', {'drinks': drinks})

@login_required
def drink_update(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == 'POST':
        form = DrinkForm(request.POST, request.FILES, instance=drink)
        if form.is_valid():
            form.save()
            return redirect('drink_list')
    else:
        form = DrinkForm(instance=drink)
    return render(request, 'drink_update.html', {'form': form})

@login_required
def drink_delete(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == 'POST':
        drink.delete()
        return redirect('drink_list')
    return render(request, 'drink_delete.html', {'drink': drink})

@login_required
def food_order(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'food_order.html', {'food': food})

@login_required
def drink_order(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    return render(request, 'drink_order.html', {'drink': drink})

# this is admin or staff who deliver orders
@login_required
def order_process(request, item_type, pk):
    # Fetch the item based on item_type and pk
    if item_type == 'food':
        item = get_object_or_404(Food, pk=pk)
    elif item_type == 'drink':
        item = get_object_or_404(Drink, pk=pk)
    else:
        return HttpResponse("Invalid item type", status=400)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            comments = form.cleaned_data['comments']
            status = form.cleaned_data['status']
            
            if quantity <= 0:
                return HttpResponse("Quantity must be greater than zero.", status=400)
            
            # Save the order with the logged-in user
            Order.objects.create(
                user=request.user,  # Associate order with the current user
                item_type=item_type,
                item_id=item.id,
                quantity=quantity,
                comments=comments,
                status='pending'
            )
            
            # Redirect to the order list page after placing the order
            # return redirect('order_list')
            return redirect('my_orders')
    else:
        form = OrderForm()
    
    return render(request, 'order_process.html', {'form': form, 'item': item, 'item_type': item_type})

@login_required
def order_complete(request, pk, item_type):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        comments = request.POST.get('comments')

        # Validate item_type and fetch the corresponding item
        if item_type == 'food':
            item = get_object_or_404(Food, pk=pk)
        elif item_type == 'drink':
            item = get_object_or_404(Drink, pk=pk)
        else:
            return HttpResponse("Invalid item type", status=400)

        # Create and save the order
        Order.objects.create(
            item_type=item_type,
            item_id=pk,
            quantity=quantity,
            comments=comments
        )

        # Redirect to the order list page after placing the order
        return redirect('order_list')
    elif request.method == 'GET':
        return HttpResponse("Order completion page", status=200)
    return HttpResponse(status=405)  # Method not allowed

@login_required
def order_list(request):
    orders = Order.objects.all().order_by('-created_at')
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def my_orders(request):
    # Fetch orders that belong to the logged-in user
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    bookings = Booking.objects.filter(user=request.user).order_by('-id')
    return render(request, 'my_orders.html', {'orders': orders, 'bookings': bookings})
