from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test

def register_view(request):
    is_admin = request.user.is_authenticated and request.user.is_staff
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, initial={'is_admin': is_admin})
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm(initial={'is_admin': is_admin})

    return render(request, 'register.html', {'form': form})



from django.urls import reverse, NoReverseMatch

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.POST.get('next', request.GET.get('next', ''))
            
            if not next_url:
                next_url = settings.LOGIN_REDIRECT_URL
            
            try:
                return redirect(next_url)
            except NoReverseMatch:
                return redirect(settings.LOGIN_REDIRECT_URL)  # Fallback to a valid URL if next_url is invalid
    else:
        form = AuthenticationForm()

    next_url = request.GET.get('next', '')
    return render(request, 'login.html', {'form': form, 'next': next_url})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to your desired page
