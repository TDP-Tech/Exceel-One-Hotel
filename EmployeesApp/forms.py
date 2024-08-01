from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'middle_name', 'last_name', 'role', 'email', 'phone_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control col-md-10', 'placeholder': 'Enter first name'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control col-md-10', 'placeholder': 'Enter middle name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control col-md-10', 'placeholder': 'Enter last name'}),
            'role': forms.TextInput(attrs={'class': 'form-control col-md-10', 'placeholder': 'Enter role/position'}),
            'email': forms.EmailInput(attrs={'class': 'form-control col-md-10', 'placeholder': 'Enter email address'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control col-md-10', 'placeholder': 'Enter phone number'}),
        }
        labels = {
            'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name',
            'role': 'Role/Position',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
        }
