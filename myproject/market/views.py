from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.core.serializers import serialize
from .serializers import *
from django.shortcuts import get_object_or_404
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
    book = get_object_or_404(Book, pk=product_id)
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


def json_request_with_serialization_framework(request):
    queryset = Book.objects.all()
    serializer = MyModelSerializer(queryset, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False)


def json_request_with_serialization(request):
    books = Book.objects.all()
    serialized_data = serialize('json', books, fields=('name', 'page_count', 'category', 'author',
                                                       'price', 'image', 'published'), use_natural_foreign_keys=True,
                                use_natural_primary_keys=True)
    return JsonResponse(serialized_data, safe=False)


def json_request_with_values_list(request):
    books = Book.objects.all().values_list(
        'name', 'page_count', 'category__name', 'author__name', 'price', 'image', 'published'
    )
    array_response_data = []
    for book_data in books:
        response_data = {
            'name': book_data[0],
            'page_count': book_data[1],
            'category': book_data[2],
            'author': book_data[3],
            'price': book_data[4],
            'image': book_data[5],
            'published': book_data[6]
        }
        array_response_data.append(response_data)

    return JsonResponse(array_response_data, safe=False)


def default_route(request, route):
    return HttpResponseNotFound("Page not found")
