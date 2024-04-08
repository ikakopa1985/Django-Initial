from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.


def index(request):
    books = Book.objects.all()
    category = Category.objects.all()
    author = Author.objects.all()
    context = {
        'books': books,
        'category': category,
        'author': author
    }
    return render(request, 'market/index.html', context)


def by_category(request, category_id):
    print("by_category")
    books = Book.objects.filter(category_id=category_id)
    category = Category.objects.all()
    author = Author.objects.all()
    category_name = Category.objects.get(id=category_id)
    context = {
        'books': books,
        'category': category,
        'filter_name': category_name,
        'author': author
    }
    return render(request, 'market/index.html', context)


def by_author(request, author_id):
    print("by_author")
    books = Book.objects.filter(author_id=author_id)
    category = Category.objects.all()
    author = Author.objects.all()
    author_name = Author.objects.get(id=author_id)
    context = {
        'books': books,
        'category': category,
        'author': author,
        'filter_name': author_name
    }
    return render(request, 'market/index.html', context)


def product(request, product_id):
    book = Book.objects.get(id=product_id)
    category = Category.objects.all()
    author = Author.objects.all()
    context = {
        'book': book,
        'category': category,
        'author': author,
    }
    return render(request, 'market/product.html', context)


def json_request(request):
    array_response_data = []
    response_data = {}
    book = Book.objects.all()
    for item in book:
        response_data['name'] = item.name
        response_data['page_count'] = item.page_count
        response_data['category'] = item.category.name
        response_data['author'] = item.author.name
        response_data['price'] = item.price
        response_data['image'] = item.image.url
        response_data['published'] = item.published
        array_response_data.append(response_data)
    print(array_response_data)
    return JsonResponse(array_response_data, safe=False)
