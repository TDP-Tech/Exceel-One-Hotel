# models.py

from django.db import models

class SlideImage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='carousel_images/')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    customer_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()  # E.g., 1 to 5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    customer_image = models.ImageField(upload_to='review_images/', blank=True, null=True)  # New field

    def __str__(self):
        return self.customer_name

class HotelImage(models.Model):
    image = models.ImageField(upload_to='images/hotel/', blank=True, null=True)

    def __str__(self):
        return "Hotel Image"

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    subscription_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class TeamMember(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_members/')

    def __str__(self):  
        return self.full_name