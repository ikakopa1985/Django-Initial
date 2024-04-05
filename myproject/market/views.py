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
    return HttpResponse('category')