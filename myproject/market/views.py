from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from django.core.serializers import serialize
from .serializers import *
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *


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
    # category_name = Category.objects.get(id=category_id)
    category_name = get_object_or_404(Category, pk=category_id)
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
    # author_name = Author.objects.get(id=author_id)
    author_name = get_object_or_404(Author, pk=author_id)
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
    return JsonResponse(array_response_data, safe=False, json_dumps_params={'ensure_ascii': False})


def json_request_with_serialization_framework(request):
    queryset = Book.objects.all()
    serializer = MyModelSerializer(queryset, many=True)
    print(serializer.data)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


def json_request_with_serialization(request):
    books = Book.objects.all()
    serialized_data = serialize('json', books, fields=('name', 'page_count', 'category', 'author',
                                                       'price', 'image', 'published'), use_natural_foreign_keys=True,
                                use_natural_primary_keys=True)
    return JsonResponse(serialized_data, safe=False, json_dumps_params={'ensure_ascii': False})


def json_request_with_values_list(request):
    books = list(
        Book.objects.all().values_list(
            'name', 'page_count', 'category__name', 'author__name', 'price', 'image', 'published', named=True))
    return JsonResponse(books, safe=False, json_dumps_params={'ensure_ascii': False})


def default_route(request, route):
    return HttpResponseNotFound("Page not found")


class AuthorCrateView(CreateView):
    template_name = 'market/create.html'
    form_class = AuthorForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.all()
        context['category'] = Category.objects.all()
        return context


class CategoryCrateView(CreateView):
    template_name = 'market/create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.all()
        context['category'] = Category.objects.all()
        return context


class BookCrateView(CreateView):
    template_name = 'market/create.html'
    form_class = BookForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Author.objects.all()
        context['category'] = Category.objects.all()
        return context
