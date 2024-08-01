# views.py

from django.shortcuts import render
from .models import SlideImage
from FoodDrinksApp.models import Food, Drink
from datetime import datetime


def home(request):
    current_year = datetime.now().year
    foods = Food.objects.all()
    drinks = Drink.objects.all()
    carousel_images = SlideImage.objects.filter(is_active=True)
    return render(request, 'home.html', {
        'foods': foods,
        'drinks': drinks,
        'carousel_images': carousel_images,
        'map_api_key': 'YOUR_GOOGLE_MAPS_API_KEY'
    })
