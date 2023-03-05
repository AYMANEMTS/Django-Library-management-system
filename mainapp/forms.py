from django import forms
from .models import Book,Catego


class AddCatego(forms.ModelForm):
    class Meta:
        model = Catego
        fields = ['name']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
        }

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'img_book',
            'img_author',
            'pages',
            'price',
            'retal_day',
            'retal_period',
            'staus',
            'category',
            'total_rental',
        ]
        widgets = {
            'title':forms.TextInput(attrs={'class':' form-control'}),
            'author':forms.TextInput(attrs={'class':' form-control'}),
            'img_book':forms.FileInput(attrs={'class':'form-control'}),
            'img_author':forms.FileInput(attrs={'class':'form-control'}),
            'pages':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'retal_day':forms.NumberInput(attrs={'class':'form-control'}),
            'retal_period':forms.NumberInput(attrs={'class':'form-control'}),
            'total_rental':forms.NumberInput(attrs={'class':'form-control'}),
            'staus':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-control'}),

        }