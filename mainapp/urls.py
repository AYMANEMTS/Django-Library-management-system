from django.urls import path
from .views import index,books,update


urlpatterns = [
    path('',index,name='index'),
    path('books',books,name='books'),
    path('/<int:id>/',update,name='update'),
]
