from django.forms import ModelForm

from .models import *
from django import forms


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('name',)


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('category', 'author', 'name', 'page_count', 'price', 'image')

    widgets = {
        'image': forms.ClearableFileInput(attrs={'multiple': False}),
    }
