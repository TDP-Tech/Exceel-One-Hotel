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
    
    path('food_order/<int:pk>/', views.food_order, name='food_order'),
    path('drink_order/<int:pk>/', views.drink_order, name='drink_order'),
    
    path('order_process/<str:item_type>/<int:pk>/', views.order_process, name='order_process'),
    
    ###########
    path('orders/<int:pk>/update/', views.order_update, name='order_update'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),
    ###########
    path('order_complete/<int:pk>/<str:item_type>/', views.order_complete, name='order_complete'),
    path('orders/', views.order_list, name='order_list'),
    path('my-orders/', views.my_orders, name='my_orders'),
]
