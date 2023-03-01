from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    context = {
        'Book':Book.objects.all()
    }
    print(context)
    return render(request,'pages/index.html',context)