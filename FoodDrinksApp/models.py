from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):
    food_name = models.CharField(max_length=100)
    food_price = models.DecimalField(max_digits=12, decimal_places=2)
    food_amount = models.PositiveIntegerField()
    food_image = models.ImageField(upload_to='food_images/', blank=True, null=True)

    def __str__(self):
        return self.food_name

class Drink(models.Model):
    drink_name = models.CharField(max_length=100)
    drink_size = models.CharField(max_length=50)
    drink_price = models.DecimalField(max_digits=12, decimal_places=2)
    drink_amount = models.PositiveIntegerField()
    drink_image = models.ImageField(upload_to='drink_images/', blank=True, null=True)

    def __str__(self):
        return self.drink_name

class Order(models.Model):
    ORDER_TYPES = [
        ('food', 'Food'),
        ('drink', 'Drink'),
    ]
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('received', 'Received'),
        ('processed', 'Processed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=ORDER_TYPES)
    item_id = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    food = models.ForeignKey(Food, null=True, blank=True, on_delete=models.SET_NULL)
    drink = models.ForeignKey(Drink, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Order {self.pk} for {self.item_type} {self.item_id}"
    
    def get_item_name(self):
        if self.item_type == 'food':
            try:
                item = Food.objects.get(pk=self.item_id)
                return item.food_name
            except Food.DoesNotExist:
                return 'Unknown Food Item'
        elif self.item_type == 'drink':
            try:
                item = Drink.objects.get(pk=self.item_id)
                return item.drink_name
            except Drink.DoesNotExist:
                return 'Unknown Drink Item'
        return 'Unknown Item'
