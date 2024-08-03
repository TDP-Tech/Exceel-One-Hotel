from django import forms
from .models import Review, NewsletterSubscriber

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['customer_name', 'rating', 'comment', 'customer_image']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Rate from 1 to 5'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your review here...',
            }),
            'customer_image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            }),
        }


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter your email',
                'required': True,
                'class': 'form-control',
            }),
        }
        labels = {
            'email': '',
        }
