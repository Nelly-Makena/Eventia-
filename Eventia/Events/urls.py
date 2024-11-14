from django.urls import path
from .views import home_view # Import your views module

urlpatterns = [
    path('', home_view, name='home'),  # Home page URL
]
