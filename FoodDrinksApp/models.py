from django.db import models

class Food(models.Model):
    food_name = models.CharField(max_length=100)
    food_price = models.DecimalField(max_digits=12, decimal_places=2)  # Adjusted for larger values
    food_amount = models.PositiveIntegerField()
    food_image = models.ImageField(upload_to='food_images/', blank=True, null=True)  # New field for images

    def __str__(self):
        return self.food_name

class Drink(models.Model):
    drink_name = models.CharField(max_length=100)
    drink_size = models.CharField(max_length=50)
    drink_price = models.DecimalField(max_digits=12, decimal_places=2)  # Adjusted for larger values
    drink_amount = models.PositiveIntegerField()
    drink_image = models.ImageField(upload_to='drink_images/', blank=True, null=True)  # New field for images

    def __str__(self):
        return self.drink_name

