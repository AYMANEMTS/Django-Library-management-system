from django.shortcuts import render,redirect , get_object_or_404
from .models import Book,Catego
from .forms import AddBookForm , AddCatego
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/account/login')
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
        'lenghtbook':Book.objects.filter(active=True).count(),
        'availble':Book.objects.filter(staus='available').count(),
        'rental':Book.objects.filter(staus='rental').count(),
        'sold':Book.objects.filter(staus='sold').count(),
        
    }
    
    return render(request,'pages/index.html',context)


@login_required(login_url='/account/login')
def books(request):

    search = Book.objects.all()
    title = None      
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains = title )


    context = {
        'catego':Catego.objects.all(),
        'Book':search,
        'formcat':AddCatego(),
        
    }
    return render(request,'pages/books.html',context)

def update(request, slug):
    slug = Book.objects.get(slug=slug)
    if request.method == 'POST':
        book_save = AddBookForm(request.POST , request.FILES , instance=slug)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = AddBookForm(instance=slug)
    context = {
        'form':book_save,
    }
    return render(request,'pages/update.html',context)
        

def delet(request , slug):
    bok_delet = get_object_or_404(Book , slug=slug)
    if request.method == 'POST':
        bok_delet.delete()
        return redirect('/')
    context = {
        'book':Book.objects.all()
    }
    return render(request,'pages/delete.html',context)