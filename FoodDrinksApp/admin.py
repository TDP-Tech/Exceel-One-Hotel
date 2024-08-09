from django.contrib import admin
from .models import Food, Drink, Order

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'food_price', 'food_amount', 'food_image')
    search_fields = ('food_name',)

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('drink_name', 'drink_size', 'drink_price', 'drink_amount', 'drink_image')
    search_fields = ('drink_name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_type','get_item_name', 'item_id', 'quantity', 'status', 'created_at')
    list_filter = ('item_type', 'created_at', 'status')
    search_fields = ('item_id', 'comments', 'status')
    ordering = ('-created_at',)
admin.site.register(Order, OrderAdmin)