from django.shortcuts import render  # For rendering templates
from django.http import HttpResponse  # Optional if returning plain text or other HTTP responses
from django.urls import reverse  # Optional if you need to reverse a URL
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import EventOrganizerForm
from .models import EventOrganizer

def home_view(request):

    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']  # Add a password confirmation field

        # Check if passwords match
        if password != password_confirm:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'register.html')

        # Check if username exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'register.html')

        # Create user
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Registration successful! Please log in.')
        return redirect('login')  # Redirect to login after successful signup

    return render(request, 'register.html')


# Sign In View
def login_view(request):



    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Basic form validation
        if not username or not password:
            messages.error(request, "Username and password are required.")
            return render(request, "login.html")

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('events')  # Redirect to homepage after successful login
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, "login.html")

    return render(request, "login.html")

@login_required
def pricing_view(request):

    return render(request, 'pricing.html')

@login_required
def subscription_view(request):

    return render(request, 'subscription.html')
@login_required
def submit_subscription_view(request):
    if request.method == "POST":
        messages.success(request, "Subscription successful! Thank you for subscribing.")
        return redirect('subscription')
    return render(request, 'subscription.html')



@login_required
def events_view(request):
    return render(request, 'events.html')
@login_required
def help_view(request):
    return render(request, 'help.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def listing_view(request):
    try:
        organizer = EventOrganizer.objects.get(user=request.user)
    except EventOrganizer.DoesNotExist:
        return redirect('profile')

    if request.method == 'POST':
        form = EventListingForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = organizer
            event.save()
            return redirect('events')
    else:
        form = EventListingForm()

    return render(request, 'listing.html', {'EventListingForm': EventListingForm})

@login_required
def organizer_profile(request):
    # Check if user already has a profile
    if EventOrganizer.objects.filter(user=request.user).exists():
        return redirect('listing')  # Redirect to event listing if profile exists

    if request.method == 'POST':
        form = EventOrganizerForm(request.POST, request.FILES)
        if form.is_valid():
            organizer = form.save(commit=False)
            organizer.user = request.user  # Assign the logged-in user
            organizer.save()
            return redirect('listing')
    else:
        form = EventOrganizerForm()

    return render(request, 'profile.html', {'EventOrganizerForm': EventOrganizerForm})
