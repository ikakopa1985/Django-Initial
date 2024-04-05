from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    books = Book.objects.all()
    category = Category.objects.all()
    context = {
        'books': books,
        'category':category
    }
    return render(request, 'market/index.html', context)

def by_category(request, category_id):
    books = Book.objects.filter(category_id=category_id)
    category = Category.objects.all()
    category_name = Category.objects.get(id=category_id)
    context = {
        'books': books,
        'category':category,
        'category_name':category_name
    }
    return render(request, 'market/by_category.html', context)