from .serializers import *
from .forms import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView


class ProductDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = ProducDetailedSerializer
    lookup_url_kwarg = 'product_id'


class ProductListView(ListAPIView):
    queryset = Book.objects.all()
    lookup_field = 'pk'
    serializer_class = ProducSerializer


class UpdateStockAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    lookup_url_kwarg = 'product_id'
    serializer_class = BookUpdateSerializer


class DeleteBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_url_kwarg = 'product_id'
