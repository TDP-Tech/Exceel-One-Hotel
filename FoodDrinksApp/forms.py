from django import forms
from .models import Food, Drink, Order

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name', 'food_price', 'food_amount', 'food_image']
        widgets = {
            'food_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter food name'}),
            'food_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter food price'}),
            'food_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount of food plates'}),
            'food_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'food_name': 'Food Name',
            'food_price': 'Food Price',
            'food_amount': 'Food Amount',
            'food_image': 'Food Image',
        }

class DrinkForm(forms.ModelForm):
    class Meta:
        model = Drink
        fields = ['drink_name', 'drink_size', 'drink_price', 'drink_amount', 'drink_image']
        widgets = {
            'drink_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter drink name'}),
            'drink_size': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter drink size'}),
            'drink_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter drink price'}),
            'drink_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount of drinks'}),
            'drink_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'drink_name': 'Drink Name',
            'drink_size': 'Drink Size',
            'drink_price': 'Drink Price',
            'drink_amount': 'Drink Amount',
            'drink_image': 'Drink Image',
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'comments', 'status']
        labels = {
            'quantity': 'Quantity',
            'comments': 'Additional Comments',
            'status': 'Order Status',
        }
        widgets = {
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter quantity of plates',
                'min': 1,
            }),
            'comments': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter any special instructions or comments here',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }

