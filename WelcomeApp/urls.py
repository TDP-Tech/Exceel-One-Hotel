from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reviews/', views.reviews, name='reviews'),
    path('subscribe/', views.newsletter_subscribe, name='subscribe'),
    path('contact/', views.contact_view, name='contact'),
    
]
