from django.urls import path 
from .views import UserRegisterView

urlpatterns = [
    path('home/register/', UserRegisterView.as_view(), name="register")
]