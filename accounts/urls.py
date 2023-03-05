from django.urls import path
from django.contrib.auth import login,logout





from django.urls import path
from .views import MyLoginView, MyLogoutView, MyRegisterView, MyProfileView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('register/', MyRegisterView.as_view(), name='register'),
    path('profile/', MyProfileView.as_view(), name='profile'),
]
