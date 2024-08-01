from django import forms
from .models import Food, Drink

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'food_price', 'food_amount']
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter food name'}),
            'food_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter food price'}),
            'food_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount of food plates'}),
        }
        labels = {
            'food_name': 'Food Name',
            'food_price': 'Food Price',
            'food_amount': 'Food Amount',
        }

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['drink_name', 'drink_size', 'drink_price', 'drink_amount']
        widgets = {
            'drink_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter drink name'}),
            'drink_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter drink size'}),
            'drink_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter drink price'}),
            'drink_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount of drinks'}),
        }
        labels = {
            'drink_name': 'Drink Name',
            'drink_size': 'Drink Size',
            'drink_price': 'Drink Price',
            'drink_amount': 'Drink Amount',
        }
