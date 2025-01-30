from django.shortcuts import render  # For rendering templates
from django.http import HttpResponse  # Optional if returning plain text or other HTTP responses
from django.urls import reverse  # Optional if you need to reverse a URL
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def home_view(request):

    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('login')  # Redirect to sign-in after successful signup
        else:
            return render(request, 'register.html', {'error': 'Username already exists!'})
    return render(request, 'register.html')


# Sign In View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Replace with your homepage URL name
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

def pricing_view(request):

    return render(request, 'pricing.html')

def subscription_view(request):

    return render(request, 'subscription.html')
def submit_subscription_view(request):
    if request.method == "POST":
        messages.success(request, "Subscription successful! Thank you for subscribing.")
        return redirect('subscription')
    return render(request, 'subscription.html')

def features_view(request):
    return render(request, 'features.html')

def events_view(request):
    return render(request, 'events.html')


