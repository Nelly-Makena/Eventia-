from django.urls import path
from .views import home_view,register_view,login_view # Import your views module

urlpatterns = [
    path('', home_view, name='home'),  # Home page URL
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
