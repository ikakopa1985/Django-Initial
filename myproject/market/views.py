from .serializers import *
from django.shortcuts import get_object_or_404
from .forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView


class ProductDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = ProducDetailedSerializer
    lookup_url_kwarg = 'product_id'


class ProductListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = ProducSerializer


@api_view()
def delete(request, product_id):
    book = get_object_or_404(Book, id=product_id)
    book.delete()
    return Response({'deleted': 'Yes'})


@api_view()
def update(request, product_id, stock):
    book = get_object_or_404(Book, id=product_id)
    book.stock = stock
    book.save()
    return Response({'updated': 'Yes'})
