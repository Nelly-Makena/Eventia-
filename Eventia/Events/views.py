from django.shortcuts import render  # For rendering templates
from django.http import HttpResponse  # Optional if returning plain text or other HTTP responses
from django.urls import reverse  # Optional if you need to reverse a URL

def home_view(request):

    return render(request, 'home.html')

