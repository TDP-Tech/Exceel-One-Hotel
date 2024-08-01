from django.shortcuts import render, redirect, get_object_or_404
from .models import Food, Drink
from .forms import FoodForm, DrinkForm

# Food Views
def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'food_create.html', {'form': form})

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'food_update.html', {'form': form})

def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('food_list')
    return render(request, 'food_delete.html', {'food': food})

# Drink Views
def drink_create(request):
    if request.method == 'POST':
        form = DrinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('drink_list')
    else:
        form = DrinkForm()
    return render(request, 'drink_create.html', {'form': form})

def drink_list(request):
    drinks = Drink.objects.all()
    return render(request, 'drink_list.html', {'drinks': drinks})

def drink_update(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == 'POST':
        form = DrinkForm(request.POST, instance=drink)
        if form.is_valid():
            form.save()
            return redirect('drink_list')
    else:
        form = DrinkForm(instance=drink)
    return render(request, 'drink_update.html', {'form': form})

def drink_delete(request, pk):
    drink = get_object_or_404(Drink, pk=pk)
    if request.method == 'POST':
        drink.delete()
        return redirect('drink_list')
    return render(request, 'drink_delete.html', {'drink': drink})
