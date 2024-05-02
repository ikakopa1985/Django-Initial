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

    def perform_update(self, serializer):
        stock = self.request.data.get('stock')
        serializer.save(stock=stock)


class DeleteBookAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    lookup_url_kwarg = 'product_id'

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
