from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from courses.models import Course, Enrollment
from purchases.models import PurchaseRequest
from django.contrib.auth import authenticate, login as auth_login

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Don't try to authenticate again, just login the saved user directly
            user.backend = 'django.contrib.auth.backends.ModelBackend'  # Set the backend
            login(request, user)
            messages.success(request, f'Welcome {user.username}! Your account has been created successfully.')
            return redirect('home')
        else:
            # Show form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    user_courses = Enrollment.objects.filter(user=request.user)
    purchase_requests = PurchaseRequest.objects.filter(user=request.user).order_by('-created_at')[:5]
    
    context = {
        'user_courses': user_courses,
        'purchase_requests': purchase_requests,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def my_courses(request):
    enrollments = Enrollment.objects.filter(user=request.user)
    return render(request, 'accounts/my_courses.html', {'enrollments': enrollments})

@login_required
def my_purchases(request):
    purchases = PurchaseRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'accounts/my_purchases.html', {'purchases': purchases})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Try to authenticate with username
        user = authenticate(request, username=username, password=password)
        
        # If that fails, try with email
        if user is None:
            try:
                user_obj = User.objects.get(email=username)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Welcome back!')
            next_page = request.GET.get('next', 'home')
            return redirect(next_page)
        else:
            messages.error(request, 'Invalid username/email or password.')
    
    return render(request, 'accounts/login.html')
