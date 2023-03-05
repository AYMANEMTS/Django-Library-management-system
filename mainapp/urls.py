from django.urls import path
from .views import index,books,update,delet


urlpatterns = [
    path('',index,name='index'),
    path('books',books,name='books'),
    path('update/<str:slug>/',update,name='update'),
    path('delet/<str:slug>/',delet,name='delet'),
]
