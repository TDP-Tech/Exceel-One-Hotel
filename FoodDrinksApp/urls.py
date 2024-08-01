from django.urls import path
from . import views

urlpatterns = [
    # Food URLs
    path('food-list/', views.food_list, name='food_list'),
    path('food/create/', views.food_create, name='food_create'),
    path('food/update/<int:pk>/', views.food_update, name='food_update'),
    path('food/delete/<int:pk>/', views.food_delete, name='food_delete'),
    
    # Drink URLs
    path('drink-list/', views.drink_list, name='drink_list'),
    path('drink/create/', views.drink_create, name='drink_create'),
    path('drink/update/<int:pk>/', views.drink_update, name='drink_update'),
    path('drink/delete/<int:pk>/', views.drink_delete, name='drink_delete'),
]
