from django.urls import path
from . import views

urlpatterns = [
    path('', views.announcement_list, name='announcement_list'),
    path('create/', views.announcement_create, name='announcement_create'),
    path('update/<int:pk>/', views.announcement_update, name='announcement_update'),
    path('delete/<int:pk>/', views.announcement_delete, name='announcement_delete'),
]
