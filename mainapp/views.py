from django.shortcuts import render,redirect
from .models import Book,Catego
from .forms import AddBookForm , AddCatego
# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = AddBookForm(request.POST , request.FILES)
        if add_book.is_valid():
            add_book.save()

        add_cat = AddCatego(request.POST)
        if add_cat.is_valid():
            add_cat.save()
        


    context = {
        'catego':Catego.objects.all(),
        'Book':Book.objects.all(),
        'form':AddBookForm(),
        'formcat':AddCatego(),
    }
    
    return render(request,'pages/index.html',context)

def books(request):
    context = {
        'catego':Catego.objects.all(),
        'Book':Book.objects.all(),
        
    }
    return render(request,'pages/books.html',context)

def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = AddBookForm(request.POST , request.FILES , instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = AddBookForm(instance=book_id)
    context = {
        'form':book_save,
    }
    return render(request,'pages/update.html',context)
        