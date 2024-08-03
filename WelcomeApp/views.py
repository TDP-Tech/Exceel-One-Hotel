# views.py

from django.shortcuts import render, redirect
from .models import SlideImage, Review, HotelImage
from FoodDrinksApp.models import Food, Drink
from datetime import datetime
from django.db.models import Avg, Count
from .forms import ReviewForm, NewsletterSubscriptionForm
from django.contrib import messages


def home(request):
    foods = Food.objects.all()
    drinks = Drink.objects.all()
    images = SlideImage.objects.filter(is_active=True)
    return render(request, 'home.html', {
        'foods': foods,
        'drinks': drinks,
        'images': images,
    })



def about(request):
    hotel_images = HotelImage.objects.all()
    # Calculate average rating and total number of reviews
    review_stats = Review.objects.aggregate(
        average_rating=Avg('rating'),
        total_reviews=Count('id')
    )

    average_rating = review_stats['average_rating'] or 0
    total_reviews = review_stats['total_reviews']

    context = {
        'hotel_images': hotel_images,
        'average_rating': average_rating,
        'total_reviews': total_reviews,
        'reviews': Review.objects.all()[:3]  # Fetching top 3 reviews for display
    }
    return render(request, 'about.html', context)

from django.conf import settings
def reviews(request):
    reviews = Review.objects.all().order_by('-id')
    total_reviews = reviews.count()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reviews')  # Redirect to the same page after saving
    else:
        form = ReviewForm()

    # Fetch default image URL from settings or database
    default_image_url = settings.DEFAULT_REVIEW_IMAGE_URL  # Ensure this is set in settings.py

    return render(request, 'reviews.html', {
        'reviews': reviews,
        'total_reviews': total_reviews,
        'average_rating': average_rating,
        'form': form,
        'default_image_url': default_image_url,
    })

def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully subscribed to the newsletter.')
            return redirect('home')
    else:
        form = NewsletterSubscriptionForm()
    return render(request, 'footer.html', {'form': form})