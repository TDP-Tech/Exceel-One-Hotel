from django.contrib import admin
from .models import Food, Drink

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'food_price', 'food_amount', 'food_image')
    search_fields = ('food_name',)

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('drink_name', 'drink_size', 'drink_price', 'drink_amount', 'drink_image')
    search_fields = ('drink_name',)
