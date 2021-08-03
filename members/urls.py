from django.urls import path 
from .views import UserRegisterView

urlpatterns = [
    path('blog/register/', UserRegisterView.as_view(), name="register")
]