from django.urls import path
from .views import home_view,register_view,login_view,pricing_view,subscription_view,submit_subscription_view# Import your views module

urlpatterns = [
    path('', home_view, name='home'),  # Home page URL
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('pricing/', pricing_view, name='pricing'),
    path('subscription/',subscription_view,name='subscription'),
    path('subscription/submit/', submit_subscription_view, name='submit_subscription'),

]
